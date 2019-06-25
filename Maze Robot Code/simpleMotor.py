from motorInterface import MotorInterface
from lineTrackerInterface import TrackerInterface
import time

'''
The simple motor class uses the motor interface with predefined values that were found out by testing.
Can give back the interface, so that other times are possible to use by using the returned interface object
'''
class SimpleMotor:
    #Instanciates the class
    def __init__(self,tracker):
        self.motor = MotorInterface()
        self.tracker = tracker

    '''
    Goes one second forward
    '''
    def forward(self):
        self.motor.forward(1)

    '''
    Goes one second backward
    '''
    def back(self):
        self.motor.back(1)

    '''
    Goes thirdy-four second forward
    Waits one second
    Turns robot left for third-five seconds
    '''
    def left(self):
        self.motor.forward(35)
        time.sleep(1)
        self.motor.left(36)

    '''
    Goes thirdy-three and a half second forward
    Waits one second
    Turns robot right for third-five and a half seconds
    '''
    def right(self):
        self.motor.forward(35)
        time.sleep(1)
        self.motor.right(36)

    '''
    Turns the robot 180 degrees
    '''
    def uturn(self):
        self.motor.left(36.5)
        time.sleep(1)
        self.motor.forward(3)
        time.sleep(1)
        self.motor.left(36.5)
        time.sleep(1)
        self.motor.back(40)


    '''
    Disables the motor
    '''
    def disable(self):
        self.motor.disable()

    '''
    Enables the motor
    '''
    def enable(self):
        self.motor.enable()

    '''
    Gets the interface of the motor
    '''
    def getInterface(self):
        return self.motor
