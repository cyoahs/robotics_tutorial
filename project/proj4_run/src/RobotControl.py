import pybullet as p
import Helper
# import AnswerByTA

def loadRobot(initPos):
    robotName = 'MarioTheRobot.urdf'
    initOrn = [1.0, 0.0, 0.0, 0.0]
    return p.loadURDF(Helper.findURDF(robotName), initPos, initOrn)

def generateTraj(robotId):
    # work in this function to make a plan before actual control
    # the output can be in any data structure you like
    plan = None
    # plan = AnswerByTA.generateTraj(robotId)
    return plan

def realTimeControl(robotId, plan):
    # work in this function to calculate real time control signal
    # the output should be a list of two float
    controlSignal = [50, 50]
    # controlSignal = AnswerByTA.realTimeControl(robotId, plan)
    return controlSignal

def addDebugItems(robotId):
    # work in this function to add any debug visual items you need
    print(p.getJointState(robotId, 1)[0])
    pass