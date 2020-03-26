import pybullet as p
import os
import Helper
import random
import math


class Env(object):
    def __init__(self, robotId, targetPos):
        # load map and robot
        mapName = 'map.urdf'
        mapPath = Helper.findURDF(mapName)
        self.mapId = p.loadURDF(mapPath)

        targetName = 'target.urdf'
        targetPath = Helper.findURDF(targetName)
        self.targetId = p.loadURDF(targetPath, targetPos)

        self.robotId = robotId

        self.motors = []
        
        jointFrictionForce = 0.001
        for joint in range(p.getNumJoints(self.robotId)):
            p.setJointMotorControl2(self.robotId, joint, p.POSITION_CONTROL, force=jointFrictionForce)
        
        self.noise = 0.03

        self.controlMode = p.TORQUE_CONTROL
    
    def addBonusBlock(self):
        bonusBlockName = 'bonusBlock.urdf'
        self.bonusBlockId = []
        blockPos = [[6.5, 0, 4.75],
                    [12.25, 0, 1.75],
                    [19.25, 0, 1.75],
                    [24.75, 0, 2.25]]
        self.bonus = [0 for i in range(len(blockPos))]

        for block in blockPos:
            self.bonusBlockId.append(p.loadURDF(Helper.findURDF(bonusBlockName), basePosition=block))
    
    def checkBonus(self):
        for bonusId, bonusBlockId in enumerate(self.bonusBlockId):
            if self.bonus[bonusId] > 0:
                continue
            getBonus = p.getContactPoints(bodyA=self.robotId, bodyB=bonusBlockId)
            if getBonus:
                self.bonus[bonusId] = 1
    
    def cameraControl(self):
        # control camera
        robotPos = p.getLinkState(self.robotId, 2)[0]
        p.resetDebugVisualizerCamera(10.0, 0.0, 0.0, robotPos)
    
    def setMotorName(self, name):
        if len(name) > 2:
            raise RuntimeError('Too many motors')
        for jointId in range(p.getNumJoints(self.robotId)):
            jointName = p.getJointInfo(self.robotId, jointId)[1]
            if jointName.decode() in name:
                self.motors.append(jointId)
    
    def control(self, force):
        # apply force control
        # force: list of 2 float, input force signal for two engine
        for motor in range(2):
            if math.fabs(force[motor]) >= 100:
                if force[motor] > 0:
                    force[motor] = 100 * random.uniform(1 - self.noise, 1 + self.noise)
                else:
                    force[motor] = -100 * random.uniform(1 - self.noise, 1 + self.noise)
            force[motor] *= random.uniform(1 - self.noise, 1 + self.noise)
        p.setJointMotorControlArray(self.robotId, self.motors, self.controlMode, forces=force)
