import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0, -10.0)

planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("pybullet/car_3.urdf", [0, 0, 1.5], [1, 0, 0, 0])

t = 0
while t < 1200:
    p.stepSimulation()
    time.sleep(1/240)
    # wheelState0 = p.getJointState(carId, 0)
    # wheelState1 = p.getJointState(carId, 1)
    # desiredWheelState0 = wheelState0[0] + 0.1
    # desiredWheelState1 = wheelState1[0] + 0.1
    # p.setJointMotorControl2(carId, jointIndex=0, controlMode=p.POSITION_CONTROL, targetPosition=desiredWheelState0)
    # p.setJointMotorControl2(carId, jointIndex=1, controlMode=p.POSITION_CONTROL, targetPosition=desiredWheelState1)
    # t += 1