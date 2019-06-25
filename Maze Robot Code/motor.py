import RPi.GPIO as GPIO

'''
Class to send signals to the servo motors to controll the movements of the wheels
'''

class Motor:
    #Seting up the motor
    def __init__(self):
        self.IN1 = 12
        self.IN2 = 13
        self.IN3 = 20
        self.IN4 = 21
        self.ENA = 6
        self.ENB = 26

        GPIO.setmode(GPIO.BCM)
        self.__setupOutput__(self.IN1)
        self.__setupOutput__(self.IN2)
        self.__setupOutput__(self.IN3)
        self.__setupOutput__(self.IN4)
        self.__setupOutput__(self.ENA)
        self.__setupOutput__(self.ENB)

        self.PWMA = self.__setPWM__(self.ENA,1)
        self.PWMB = self.__setPWM__(self.ENB,1)
        self.__startPWM__(self.PWMA,1)
        self.__startPWM__(self.PWMB,1)

    '''
    Enables the robot's motor
    '''
    def enable(self):
        self.__high__(self.ENA)
        self.__high__(self.ENB)

    '''
    Disables the robot's motor
    '''
    def disable(self):
        self.__low__(self.ENA)
        self.__low__(self.ENB)
        GPIO.cleanup()

    '''
    Starts the robot to go forward
    '''
    def forward(self):
        self.__low__(self.IN1)
        self.__high__(self.IN2)
        self.__high__(self.IN3)
        self.__low__(self.IN4)

    '''
    Starts the robot to go backward
    '''
    def backward(self):
        self.__high__(self.IN1)
        self.__low__(self.IN2)
        self.__low__(self.IN3)
        self.__high__(self.IN4)

    '''
    Starts the robot to go left
    '''
    def left(self):
        self.__low__(self.IN1)
        self.__high__(self.IN2)
        self.__low__(self.IN3)
        self.__high__(self.IN4)

    '''
    Starts the robot to go right
    '''
    def right(self):
        self.__high__(self.IN1)
        self.__low__(self.IN2)
        self.__high__(self.IN3)
        self.__low__(self.IN4)

    '''
    Stops any movements of the robot
    '''
    def stop(self):
        self.__low__(self.IN1)
        self.__low__(self.IN2)
        self.__low__(self.IN3)
        self.__low__(self.IN4)

    '''
    Sends a low signal to a specified pin
    '''
    def __low__(self,v):
        GPIO.output(v,GPIO.LOW)

    '''
    Sends a high signal to a specified pin
    '''
    def __high__(self, v):
        GPIO.output(v,GPIO.HIGH)

    '''
    Setup specified pin as output
    '''
    def __setupOutput__(self,v):
        GPIO.setup(v,GPIO.OUT)

    '''
    Sets step size of certain motor v to n
    '''
    def __setPWM__(self,v,n):
        return GPIO.PWM(v,n)

    '''
   Sets step power of certain motor v to n
   '''
    def __startPWM__(self,v,n):
        v.start(n)
