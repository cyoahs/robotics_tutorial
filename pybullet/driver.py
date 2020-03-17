import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-10)

planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("pybullet/car_3.urdf", [0, 0, 2.0], [1, 0, 0, 0])
while True:
    pass