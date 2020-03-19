import pybullet as p
import time
import numpy as np

from Env import Env
import RobotControl

p.connect(p.GUI)

# load the plane and the table
# the height of table is 1.1
env = Env()

# load your robot here
robotId = RobotControl.load()
env.robotId = robotId

# print joint info
for jointId in range(p.getNumJoints(robotId)):
    print(p.getJointInfo(robotId, jointId))

# add your debug items
RobotControl.addDebugItems(robotId)

# Loop over 4 tests
for i in [1, 2, 4, 8]:
    # reset your robot
    for jointId in range(p.getNumJoints(robotId)):
        p.resetJointState(robotId, jointId, 0)

    # init the baseball and avoid collision between baseball and the base of the robot arm
    env.addBaseball()

    # get random target
    env.setTarget(i)

    # generate trajectory with your function, env.randPos is the position of baseball and env.randTarget is the target position
    traj = RobotControl.generateTraj(robotId, env.randPos, env.randTarget)
    trajLength = len(traj)

    # start simulation
    groundContactFlag = False
    t = 0
    while not groundContactFlag:
        # simulate
        p.stepSimulation()
        time.sleep(1/240)
        
        # contact
        env.findContact()

        # camera control
        env.cameraControl(i)

        # score
        if env.contactBetweenBallAndGround:
            groundContactFlag = True
            env.recordDistance()
            
        # control
        # work in this section
        if t < trajLength:
            p.setJointMotorControlArray(robotId, list(range(p.getNumJoints(robotId))), p.POSITION_CONTROL, targetPositions=traj[t])
            baseVel = p.getBaseVelocity(env.ballId)[0]
            print(np.linalg.norm([baseVel[:2]]))
        t += 1
        
        # end control

print(env.distance)