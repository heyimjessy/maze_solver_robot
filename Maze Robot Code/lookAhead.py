from simpleMotor import SimpleMotor
from motorInterface import MotorInterface
from lineTrackerInterface import TrackerInterface

'''
Class to check if there is a straight line before turning right.
Goes x steps forward, checks and if goes x steps back
'''
class LookAhead:
    def __init__(self,motor,tracker):
        self.motor = motor.getInterface()
        self.tracker = tracker
        self.__forward__ = 3

    def hasForward(self,ret=False):
        for i in range(0,self.__forward__):
            self.motor.forward(self.__forward__)
        if self.tracker.isOnLine():
            if ret:
                self.motor.back(self.__forward__+10)
            return True
        else:
            self.motor.back(self.__forward__+10)
            return False
