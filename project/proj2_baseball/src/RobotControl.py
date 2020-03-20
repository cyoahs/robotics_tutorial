import pybullet as p
import os
import numpy as np


def load():
    # work in the following section to load your robot
    robotName = 'HextechCatcher.urdf'
    robotPath = os.path.join('project', 'proj2_baseball', 'rsc', robotName)
    robotInitPos = [-0.6, 0.6, 1.1+0.5]
    robotInitOrn = [1.0, 0.0, 0.0, 0.0]
    robotId = p.loadURDF(robotPath, robotInitPos, robotInitOrn)
    return robotId


def generateTraj(robotId, ballPos, targetPos):
    # work in this section, generate your tarjectory as a second order list
    # e.g. traj = [[j_1(t1), j_2(t1), j_3(t1)], [j_1(t2), j_2(t2), j_3(t2)], [j_1(t3), j_2(t3), j_3(t3)], ...]
    # robotId is the Unique body index for your robot
    # ballPos is a list for the baseball position, like [x, y, z]
    # targetPos is a list for the target position, like [x, y, z]
    # do not use the inverse kinematics function of pybullet!!!!!!
    # The following code is a example for a very simple robot 

    traj = []
    numJoints = p.getNumJoints(robotId)

    # stage 1: catch the ball
    holderTopState = p.getLinkState(robotId, 3)[0]
    dx = ballPos[0] - holderTopState[0]
    dy = - (ballPos[1] - holderTopState[1])
    dz_1 = - (0.11 + 1.1 + 0.1 - holderTopState[2])
    dz_2 = 0.1
    targetJointPos1 = [dx, dy, dz_1, 0, 0, 0]
    targetJointPos2 = [dx, dy, dz_1+dz_2, 0, 0, 0]
    nStep = 240
    traj.extend([[targetJointPos1[joint]*step/nStep for joint in range(numJoints)] for step in range(nStep)])
    nStep = 120
    traj.extend([[targetJointPos1[joint] + (targetJointPos2[joint] - targetJointPos1[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])

    # stage 2: hold
    targetJointPos3 = [dx, dy, dz_1+dz_2, 0, 0.012, 0.012]
    nStep = 120
    traj.extend([[targetJointPos2[joint] + (targetJointPos3[joint] - targetJointPos2[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])
    
    # stage 3: move up
    targetJointPos4 = [dx, dy, 0, 0, 0.012, 0.012]
    nStep = 240
    traj.extend([[targetJointPos3[joint] + (targetJointPos4[joint] - targetJointPos3[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])

    # stage 4: rotate
    vec = [targetPos[0] - ballPos[0], targetPos[1] - ballPos[1]]
    rot = np.arctan2(vec[1], vec[0])
    targetJointPos5 = [dx, dy, 0, -rot, 0.02, 0.02]
    nStep = 240
    traj.extend([[targetJointPos4[joint] + (targetJointPos5[joint] - targetJointPos4[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])
    
    # stage 5: horizontal speed up
    accLength = 0.2
    horizontalLength = np.linalg.norm(vec)
    height = 0.11+0.45
    v = horizontalLength/((height/5)**0.5)
    nStep = int(accLength/v*240*0.9)
    dx_1 = accLength*np.cos(rot)
    dy_1 = -accLength*np.sin(rot)
    targetJointPos6 = [dx+dx_1*0.7, dy+dy_1*0.7, 0, -rot, 0.015, 0.015]

    traj.extend([[targetJointPos5[joint] + (targetJointPos6[joint] - targetJointPos5[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])

    # stage 6: throw
    targetJointPos7 = [dx+dx_1*0.9, dy+dy_1*0.9, 0, -rot, 0.0, 0.0]
    nStep = int(accLength/v*240*0.2)
    if nStep < 1:
        nStep = 1
    traj.extend([[targetJointPos6[joint] + (targetJointPos7[joint] - targetJointPos6[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])

    targetJointPos8 = [dx+dx_1, dy+dy_1, 0, -rot, 0.0, 0.0]
    nStep = int(accLength/v*240*0.1)
    if nStep < 1:
        nStep = 1
    traj.extend([[targetJointPos7[joint] + (targetJointPos8[joint] - targetJointPos7[joint])*step/nStep for joint in range(numJoints)] for step in range(nStep)])

    return traj


def addDebugItems(robotId):
    # add any debug Items you like
    p.addUserDebugLine([0, 0, 0], [1, 0, 0], lineColorRGB=[0.5, 0.5, 0.5], parentObjectUniqueId=robotId, parentLinkIndex=3)
    # pass