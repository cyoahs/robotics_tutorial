import pybullet as p

row, pitch, yaw = 1.57, 0, 0
quat = p.getQuaternionFromEuler([row, pitch, yaw])

x, y, z, w = 1, 0, 0, 0
rpy = p.getEulerFromQuaternion([x, y, z, w])

mat = p.getMatrixFromQuaternion([x, y, z, w])

