import pybullet as p

p.setJointMotorControl2(robotID,
                        jointID,
                        controlMode,
                        targetPosition,
                        targetVelocity,
                        force,
                        positionGain,
                        velocityGain,
                        maxVelocity,
                        physicsClientId)

