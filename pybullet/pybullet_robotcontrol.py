import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

robotID = p.loadURDF("r2d2.urdf", [0, 0, 0], [0, 0, 1, 0])

# joints
numJoint = p.getNumJoints(robotID)
linkStates = []
for linkID in range(numJoint):
    linkStates.append(p.getLinkState(robotID, linkID))

linkStates_ = p.getLinkStates(robotID, list(range(numJoint)))
baseVelocity = p.getBaseVelocity(robotID)
cubePos, cubeOrn = p.getBasePositionAndOrientation(robotID)

forceVec = [0, 0, 1]
forcePos = [0, 0, 0]
flag = p.LINK_FRAME
linkID = 1
p.applyExternalForce(robotID, linkID, forceVec, forcePos, flag)

