import pybullet as p
import time


physicsClient = p.connect(p.GUI)
p.setGravity(0,0,0)
p.setRealTimeSimulation(1)

cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
robotId = p.loadURDF("multibody.urdf",cubeStartPos, cubeStartOrientation)
pass