import pybullet as p
import time
import Helper

from Env import Env
import RobotControl

# video flag
recordVideo = False
prefix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

p.connect(p.GUI)
p.setGravity(0.0, 0.0, -10.0)

# load your robot here
initPos = [0.0, 0.0, 2.0]
robotId = RobotControl.loadRobot(initPos)

# specify the names for your motor joints in urdf file
motorName = ['engine1', 'engine2']

# load whole environment
targetPos = [41, 0.0, 1.25]

env = Env(robotId, targetPos)
env.setMotorName(motorName)
env.addBonusBlock()

plan = RobotControl.generateTraj(env.robotId)

# print infomation for all the joints
for jointId in range(p.getNumJoints(env.robotId)):
    print(p.getJointInfo(env.robotId, jointId))
    p.enableJointForceTorqueSensor(env.robotId, jointId, 1)

if recordVideo:
    videoFile = Helper.findLog(prefix+'.mp4')
    videoLogId = p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, videoFile)

t = 0
while True:
    p.stepSimulation()
    time.sleep(1/240)

    controlSignal = RobotControl.realTimeControl(env.robotId, plan)
    env.control(controlSignal)

    env.cameraControl()
    RobotControl.addDebugItems(env.robotId)
    env.checkBonus()

    t += 1/240

    reachEnd = p.getContactPoints(bodyA=env.robotId, bodyB=env.targetId)
    if reachEnd:
        break

if recordVideo:
    p.stopStateLogging(videoLogId)

with open(Helper.findLog(prefix+'.txt'), 'w') as f:
    print('Congratulatons!')
    f.writelines(f'Origin time: {t}\n')
    print(f'Origin time: {t}')
    for idx, val in enumerate(env.bonus):
        f.writelines(f'Bonus {idx+1}: {val} \n')
        print(f'Bonus {idx+1}: {val}')
    f.writelines(f'Final time: {t - sum(env.bonus)*5}\n')
    print(f'Final time: {t - sum(env.bonus)*5}')