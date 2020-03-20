import pybullet as p
import time

from Env import Env
import RobotControl

p.connect(p.GUI)
p.setGravity(0.0, 0.0, -10.0)

startPos = [-12.0, 0.0, 0.0]

env = Env(startPos)
plan = RobotControl.generateTraj(env.robotId)

for jointId in range(p.getNumJoints(env.robotId)):
    print(p.getJointInfo(env.robotId, jointId))
    p.enableJointForceTorqueSensor(env.robotId, jointId, 1)

while True:
    p.stepSimulation()
    time.sleep(1/240)

    controlSignal = RobotControl.realTimeControl(env.robotId, plan)
    env.control(controlSignal)

    env.cameraControl()
    RobotControl.addDebugItems()
