from simpleMotor import SimpleMotor
from lineTrackerInterface import TrackerInterface
from lineSeeker import LineSeeker
from lookAhead import LookAhead
import time

'''
        Drives the robot through the maze according to the path given.
        Uses the tracker to follow the line.
        If it comes out, it tries if it can come back to the line. If not, it waits for user intervention
'''
class DrivingController:
    #instanciate the controller
    def __init__(self,path,motor,tracker):
        self.path = path
        self.ind = 0
        self.tracker = tracker
        self.motor = motor
        self.seeker = LineSeeker(motor,tracker)
        self.lookAhead = LookAhead(motor,tracker)


    '''
    Runs the controller 
    '''
    def run(self):
        while not self.tracker.onFinishField():
            if self.tracker.isOnLine():
                if not self.tracker.hasRight() and not self.tracker.hasLeft():
                    self.motor.forward()
                elif not self.tracker.hasRight() and self.tracker.hasLeft():
                    if self.lookAhead.hasForward(True):
                        v = self.path[self.ind]
                        self.ind += 1
                        if v == 'S':
                            for i in range(0,5):
                                self.motor.forward()
                        elif v == 'L':
                            self.motor.left()
                    else:
                        self.motor.left()
                elif self.tracker.hasRight() and not self.tracker.hasLeft():
                    if self.lookAhead.hasForward(True):                 
                        v = self.path[self.ind]
                        self.ind += 1
                        if v == 'S':
                            for i in range(0,5):
                                self.motor.forward()
                        elif v == 'R':
                            self.motor.right()
                elif self.tracker.hasRight() and self.tracker.hasLeft():
                    if self.lookAhead.hasForward(True):
                        v = self.path[self.ind]
                        self.ind += 1
                        if v == 'S':
                            for i in range(0,5):
                                self.motor.forward()
                        elif v == 'R':
                            self.motor.right()
                        elif v == 'L':
                            self.motor.left()
                    else:
                        v = self.path[self.ind]
                        self.ind += 1
                        if v == 'R':
                            self.motor.right()
                        elif v == 'L':
                            self.motor.left()
            else:
                if self.seeker.hasDetection():
                    self.seeker.run()
                else:
                    while not self.tracker.isOnLine():
                        time.sleep(6)
