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
initPos = [0.0, 0.0, 1.5]
robotId = RobotControl.loadRobot(initPos)

# specify the names for your motor joints in urdf file
motorName = ['engine1', 'engine2']

# load whole environment
targetPos = [20.0, 0.0, 0.5]

env = Env(robotId, targetPos)
env.setMotorName(motorName)

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

    t += 1/240

    reachEnd = p.getContactPoints(bodyA=env.robotId, bodyB=env.targetId)
    if reachEnd:
        break

if recordVideo:
    p.stopStateLogging(videoLogId)

with open(Helper.findLog(prefix+'.txt'), 'w') as f:
    f.writelines(f'Total time: {t}')
print('Congratulatons!')
print(f'Total time: {t}')