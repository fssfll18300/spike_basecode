################################################################################
# mission_four.py
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

def mission_four(r: robot):
    print("Running Mission 4")
    # Your code goes here...
    r.robot.straight(400)
    r.ram.run_time(-5000,2000)
    r.robot.straight(-300)
    r.ram.run_time(2000,1000)
    r.robot.straight(300)
    r.ram.run_time(-5000,1000)
    r.robot.straight(-9999)
    # Sample code: Test the speaker

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
