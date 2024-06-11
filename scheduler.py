import schedule
import time
import os

def run_robot_file():
    # Command to run the robot file
    os.system('robot --pythonpath ./Test/cara.robot')

# Schedule the task to run every 2 hours
schedule.every(2).hours.do(run_robot_file)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
