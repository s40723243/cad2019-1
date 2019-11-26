from controller import Robot, Motor

TIME_STEP = 64

# create the Robot instance.
robot = Robot()

# get the motor devices
motor = robot.getMotor('motor')
# set the target position of the motors
motor.setPosition(10.0)

while robot.step(TIME_STEP) != -1:
   pass