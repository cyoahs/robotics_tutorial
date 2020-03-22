import pybullet as p
import time
import Helper

from Env import Env
import RobotControl

# video flag
recordVideo = True
prefix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

p.connect(p.GUI)
p.setGravity(0.0, 0.0, -10.0)

startPos = [-12.0, 0.0, 0.0]

env = Env(startPos)
plan = RobotControl.generateTraj(env.robotId)

for jointId in range(p.getNumJoints(env.robotId)):
    print(p.getJointInfo(env.robotId, jointId))
    p.enableJointForceTorqueSensor(env.robotId, jointId, 1)

if recordVideo:
    videoFile = Helper.findLog(prefix+'.mp4')
    videoLogId = p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, videoFile)

while True:
    p.stepSimulation()
    time.sleep(1/240)

    controlSignal = RobotControl.realTimeControl(env.robotId, plan)
    env.control(controlSignal)

    env.cameraControl()
    RobotControl.addDebugItems()

if recordVideo:
    p.stopStateLogging(videoLogId)
