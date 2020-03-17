import pybullet as p
import time
import pybullet_data


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-10)

planeId = p.loadURDF("plane.urdf")

cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

loggingID = p.startStateLogging(p.STATE_LOGGING_GENERIC_ROBOT, 'log.bin', maxLogDof=100)
for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)
p.stopStateLogging(loggingID)

cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()

