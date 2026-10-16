################################################################################
# mission_two.py
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

def mission_two(r: robot):
    print("Running Mission 2")
    # Your code goes here...
    r.ram.run_angle(500,30)
    r.robot.straight(550)
    #starting turbo mode
    r.robot.settings(800,1000,500,400)
    r.robot.straight(-550)
    r.robot.stop()
    #ending turbo mode
    r.robot.settings(500,500,400,400)



################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
