################################################################################
# mission_five.py
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

def mission_five(r: robot):
    print("Running Mission 5")
    # Your code goes here...
    r.robot.straight(200)
    r.robot.turn(50)
    r.robot.straight(260)
    r.lam.run_until_stalled(-9999, duty_limit=9999)
    r.robot.straight(-9999)
    #r.robot.straight(200)
    #r.robot.turn(90)
    #r.robot.straight(9999)
    #r.robot.turn(-90)
    #r.ram.run_time(1000,1000)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
