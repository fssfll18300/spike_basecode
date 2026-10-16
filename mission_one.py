################################################################################
# mission_one.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Your Name(s)]
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
#eyes = UltrasonicSensor(Port.A)

def mission_one(r: robot):
    print("Running Mission 1")
    # Your code goes here...
    #r.robot.straight(1000)
    #print("eyes",eyes.distance())
    #if eyes.distance() < 596:
        #r.robot.brake()





################################mj
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
