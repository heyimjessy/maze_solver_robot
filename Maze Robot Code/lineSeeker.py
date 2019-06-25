from simpleMotor import SimpleMotor
from motorInterface import MotorInterface
from lineTrackerInterface import TrackerInterface

'''
The Line Seeker does handle the process of finding the line again.
First it looks where the line is within the tolerance.
Then it calculates the movements necessary and performs it
'''

class LineSeeker:
    def __init__(self,motor,tracker):
        self.motor = motor.getInterface()
        self.tracker = tracker

    def run(self):
        vals = self.tracker.getValues()
        if self.hasDetection():
            left = 0
            right = 0
            if vals[0]=='1':
                left = 1
            elif vals[1]=='1':
                left = 1
            elif vals[3]=='1':
                right = 1
            elif vals[4]=='1':
                right = 1

            if left > 0:
                while not self.tracker.isOnLine():
                    self.motor.left(1)
            elif right > 0:
                while not self.tracker.isOnLine():
                    self.motor.right(1)

    def hasDetection(self):
        vals = self.tracker.getValues()
        if (vals[0:2].count('1') or vals[3:].count('1')) and vals[2]=='0':
            return True
        else:
            return False
