import pybullet as p
import pybullet_data
import os
import random
import numpy as np
import Helper


class Env(object):
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -10.0)

        self.planeId = p.loadURDF("plane.urdf")
        tableName = 'table.urdf'
        # tablePath = os.path.join('project', 'proj2_baseball', 'rsc', tableName)
        tablePath = Helper.findURDF(tableName)
        self.tableId = p.loadURDF(tablePath, [0, 0, 1.05], [1.0, 0.0, 0.0, 0.0])

        ballName = 'ball.urdf'
        # self.ballPath = os.path.join('project', 'proj2_baseball', 'rsc', ballName)
        self.ballPath = Helper.findURDF(ballName)
        targetName = 'target.urdf'
        # self.targetPath = os.path.join('project', 'proj2_baseball', 'rsc', targetName)
        self.targetPath = Helper.findURDF(targetName)

        self.distance = []
        self.score = 0
        self.robotId = 100
    
    def addBaseball(self):
        basePos, _ = p.getBasePositionAndOrientation(self.robotId)
        randPos = [random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3), 1.1+0.04]
        while np.linalg.norm(np.array(randPos[:2]) - np.array([basePos[:2]])) < 0.04:
            randPos = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 1.1+0.04]
        
        print('Ball Position:')
        print(randPos)

        self.randPos = randPos
        self.ballId = p.loadURDF(self.ballPath, randPos, [1.0, 0.0, 0.0, 0.0])

        self.catchFlag = False

    def setTarget(self, i):
        randTheta = np.pi*random.uniform(-0.5, 0.5)
        randTarget = [random.uniform(i + 1, i + 2)*np.cos(randTheta), random.uniform(i + 1, i + 2)*np.sin(randTheta), 0.0]

        print('Target position:')
        print(randTarget)

        self.randTarget = randTarget
        self.targetId = p.loadURDF(self.targetPath, randTarget, [1.0, 0.0, 0.0, 0.0])

    def findContact(self):
        self.contactBetweenBallAndGround = p.getContactPoints(bodyA=self.ballId, bodyB=self.planeId)
        self.contactBetweenBallAndRobot = p.getContactPoints(bodyA=self.ballId, bodyB=self.robotId)
        if self.contactBetweenBallAndRobot:
            self.catchFlag = True
    
    def cameraControl(self, i):
        basePos, _ = p.getBasePositionAndOrientation(self.robotId)
        if not self.catchFlag:
            # camera focus on ball
            vec = [self.randPos[0] - basePos[0], self.randPos[1] - basePos[1]]
            yaw = np.arctan2(vec[1], vec[0])/np.pi*180
            p.resetDebugVisualizerCamera(cameraDistance=3.0, cameraYaw=yaw, cameraPitch=-45, cameraTargetPosition=[0, 0, 1.1])
        else:
            # camera focus on 
            vec = [self.randPos[0] - self.randTarget[0], self.randPos[1] - self.randTarget[1]]
            yaw = np.arctan2(vec[1], vec[0])/np.pi*180
            p.resetDebugVisualizerCamera(cameraDistance=max(1.2*i, 3.0), cameraYaw=yaw, cameraPitch=-45, cameraTargetPosition=[self.randPos[0]/2 + self.randTarget[0]/2, self.randPos[1]/2 + self.randTarget[1]/2, 1.1])

    def recordDistance(self):
        self.distance.append(np.linalg.norm([self.contactBetweenBallAndGround[0][5][0] - self.randTarget[0], self.contactBetweenBallAndGround[0][5][1] - self.randTarget[1]]))
    
    def calcScore(self):
        if self.distance:
            for distance in self.distance:
                if distance < 0.1:
                    self.score += 100/4
                else:
                    self.score += 100*0.1**0.25/distance**0.25/4
        return self.score
    
    def writeLog(self, scoreFile):
        with open(scoreFile, 'w') as f:
            f.writelines('File name:\n')
            f.writelines(scoreFile+'\n')
            f.writelines('Distance:\n')
            f.writelines(f'{self.distance}\n')
            f.writelines('Score:\n')
            f.writelines(f'{self.score}\n')
