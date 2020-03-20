import pybullet as p
import time
import numpy as np
import os

from Env import Env
import RobotControl

p.connect(p.GUI)

# video flag
recordVideo = True
prefix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

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

if recordVideo:
    videoFile = os.path.join('project', 'proj2_baseball', 'log', prefix+'.mp4')
    videoLogId = p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, videoFile)

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
        t += 1
        
        # end control

if recordVideo:
    p.stopStateLogging(videoLogId)
score = env.calcScore()
print(env.distance)
print(score)
scoreFile = os.path.join('project', 'proj2_baseball', 'log', prefix+'.txt')
env.writeLog(scoreFile)
