import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0, -10.0)

planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("pybullet/car_4.urdf", [0, 0, 1.5], [1, 0, 0, 0])

t = 0
yaw = 0
while t < 1200:
    p.stepSimulation()
    time.sleep(1/240)
    wheelState0 = p.getJointState(carId, 0)
    wheelState1 = p.getJointState(carId, 1)
    desiredWheelState0 = wheelState0[0] - 0.3
    desiredWheelState1 = wheelState1[0] - 0.3
    p.setJointMotorControl2(carId, jointIndex=0, controlMode=p.POSITION_CONTROL, targetPosition=desiredWheelState0)
    p.setJointMotorControl2(carId, jointIndex=1, controlMode=p.POSITION_CONTROL, targetPosition=desiredWheelState1)

    baseOrnLineId = p.addUserDebugLine([0, 0, 0], [3, 0, 0], lineColorRGB=[1, 0, 0], parentObjectUniqueId=carId)
    WheelLineId = p.addUserDebugLine([0, 0, 1], [3, 0, 2], lineColorRGB=[0, 0, 0], parentObjectUniqueId=carId, parentLinkIndex=0)

    basePos, baseOrn = p.getBasePositionAndOrientation(carId)
    rpy = p.getEulerFromQuaternion(baseOrn)
    yaw += 0.3
    cameraYaw = rpy[2] + yaw
    cameraPitch = rpy[1] - 45
    p.resetDebugVisualizerCamera(cameraDistance=10.0, cameraYaw=cameraYaw, cameraPitch=cameraPitch, cameraTargetPosition=basePos)

    t += 1