import pybullet as p
import os


class Env(object):
    def __init__(self, initPos, robotName='HextechUAV.urdf'):
        # load map and robot
        mapName = 'forest.urdf'
        mapPath = os.path.join('project', 'proj3_fly', 'rsc', mapName)
        self.mapId = p.loadURDF(mapPath)

        mapPath = os.path.join('project', 'proj3_fly', 'rsc', robotName)
        self.initPos = initPos
        self.robotId = p.loadURDF(mapPath, initPos)

        # p.changeDynamics(self.robotId, 0, linearDamping=0.0, jointDamping=0.0)
        # p.changeDynamics(self.robotId, 1, linearDamping=0.0, jointDamping=0.0)
        # p.changeDynamics(self.robotId, 2, angularDamping=0.0, jointDamping=0.0)
        
        jointFrictionForce = 0.1
        for joint in range(p.getNumJoints(self.robotId)):
            p.setJointMotorControl2(self.robotId, joint, p.POSITION_CONTROL, force=jointFrictionForce)

    
    def cameraControl(self):
        # control camera
        robotPos = p.getLinkState(self.robotId, 2)[0]
        p.resetDebugVisualizerCamera(10.0, 0.0, 0.0, robotPos)
    
    def control(self, force):
        # apply force control
        # force: list of 2 float, input force signal for two engine
        p.applyExternalForce(self.robotId, 3, [0, 0, force[0]], [0, 0, 0], p.LINK_FRAME)
        p.applyExternalForce(self.robotId, 4, [0, 0, force[1]], [0, 0, 0], p.LINK_FRAME)

