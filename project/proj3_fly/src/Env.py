import pybullet as p
import os
import Helper
import random
import math


class Env(object):
    def __init__(self, initPos, targetPos, robotName='HextechUAV.urdf'):
        # load map and robot
        mapName = 'forest.urdf'
        mapPath = Helper.findURDF(mapName)
        self.mapId = p.loadURDF(mapPath)

        robotPath = Helper.findURDF(robotName)
        self.initPos = initPos
        self.robotId = p.loadURDF(robotPath, initPos)

        targetName = 'target.urdf'
        targetPath = Helper.findURDF(targetName)
        self.targetId = p.loadURDF(targetPath, targetPos)
        
        jointFrictionForce = 0.01
        for joint in range(p.getNumJoints(self.robotId)):
            p.setJointMotorControl2(self.robotId, joint, p.POSITION_CONTROL, force=jointFrictionForce)
        
        self.noise = 0.03
    
    def cameraControl(self):
        # control camera
        robotPos = p.getLinkState(self.robotId, 2)[0]
        p.resetDebugVisualizerCamera(15.0, 0.0, 0.0, robotPos)
    
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
        p.applyExternalForce(self.robotId, 3, [0, 0, force[0]], [0, 0, 0], p.LINK_FRAME)
        p.applyExternalForce(self.robotId, 4, [0, 0, force[1]], [0, 0, 0], p.LINK_FRAME)
