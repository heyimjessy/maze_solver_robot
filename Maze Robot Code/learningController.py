from simpleMotor import SimpleMotor
from lineTrackerInterface import TrackerInterface
from movementRecorder import MovementRecorder
from lookAhead import LookAhead
from lineSeeker import LineSeeker
import time

'''
Class to run the robot in the learning stage.
Follows line with the tracker.
When it comes off line, then it tries to come back to the line again.
If it can't find the line, it assumes a dead end and makes a uturn.
Looks ahead when there is a right turn option w/o a left turn option, to find out if there is a straight line. 
If there is a straight line, it records it, if not it goes back and makes a right turn.

'''
class LearningController:
    #Instanciate the controller
    def __init__(self,motor,tracker):
        self.motor = motor
        self.tracker = tracker
        self.recorder = MovementRecorder()
        self.lookAhead = LookAhead(motor,tracker)
        self.seeker = LineSeeker(motor,tracker)

    '''
    Runs the controller
    '''
    def run(self):
        while not self.tracker.onFinishField():
            if self.tracker.isOnLine():
                if self.tracker.hasLeft() and not self.tracker.onFinishField():
                    isIntersection = self.tracker.hasRight()
                    if not isIntersection:
                        isIntersection = self.lookAhead.hasForward(True)
                        while not self.tracker.hasLeft():
                            self.motor.forward()
                    self.motor.left()
                    if isIntersection:
                        self.recorder.left()
                elif self.tracker.hasRight() and not self.tracker.onFinishField():
                    if self.lookAhead.hasForward():
                        self.recorder.straight()
                    else:
                        self.motor.right()
                        #self.recorder.right()
                elif not self.tracker.hasLeft() and not self.tracker.hasRight() and not self.tracker.onFinishField():
                    self.motor.forward()
                elif not self.tracker.hasLeft() and not self.tracker.hasRight() and self.tracker.onFinishField():
                    self.motor.stop()
                    return True
            else:
                if self.seeker.hasDetection():
                    self.seeker.run()
                else:
                    time.sleep(6)
                    if not self.tracker.isOnLine():
                        self.motor.uturn()
                        self.recorder.back()


    '''
        Returns the path driven.
    '''
    def getPath(self):
        return self.recorder.getArray()


