import pybullet as p

# 连接物理引擎
physicsClient = p.connect(p.GUI)
# p.setGravity(0, 0, 0)
p.setGravity(0, 0, -10)

# 载入机器人
robotID = p.loadURDF("r2d2.urdf", [0, 0, 0], [0, 0, 1, 0])

# 实时模拟
p.setRealTimeSimulation(0)
# p.setRealTimeSimulation(1)

# 时间步长
p.setTimeStep(1/240) # default

# 模拟一步
p.stepSimulation()

