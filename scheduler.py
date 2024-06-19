import time
import os

hours = 1


def run_robot_file():
    # Command to run the robot file
    if os.name == 'nt':
        os.system('python -m robot .\Test\cara.robot')
    else:
        os.system('robot --pythonpath . Test/cara.robot')


def hours_to_seconds(hours):
    """Convert hours to seconds."""
    seconds = hours * 3600
    return seconds


if __name__ == "__main__":
    # Keep the script running
    while True:
        run_robot_file()
        time.sleep(hours_to_seconds(hours))
