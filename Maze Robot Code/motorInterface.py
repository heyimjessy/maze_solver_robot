from motor import Motor
import time

'''
Interface to use the motor and stop the robot after x seconds
'''
class MotorInterface:
    #Instanciates the object
    def __init__(self):
        self.motor = Motor()
        self.motor.enable()

    '''
    Goes forward x seconds
    '''
    def forward(self,tsec):
        self.motor.forward()
        time.sleep(tsec)
        self.motor.stop()

    '''
    Goes left x seconds
    '''
    def left(self,tsec):
        self.motor.left()
        time.sleep(tsec)
        self.motor.stop()

    '''
    Goes right x seconds
    '''
    def right(self,tsec):
        self.motor.right()
        time.sleep(tsec)
        self.motor.stop()

    '''
    Goes back x seconds
    '''
    def back(self,tsec):
        self.motor.backward()
        time.sleep(tsec)
        self.motor.stop()

    '''
    Stops and disables the motor
    '''
    def disable(self):
        self.motor.stop()
        self.motor.disable()

    '''
    Enables the motor
    '''
    def enable(self):
        self.motor.enable()