import RPi.GPIO as GPIO

'''
Class to read out the line sensor.
Total read out 8 times per sensor by read.
Converts the values to binary  at the end.
'''
class LineTrackerReader:
    def __init__(self):
        self.Control = 5
        self.Clock = 25
        self.Address = 24
        self.DataIn = 23

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.Clock, GPIO.OUT)
        GPIO.setup(self.Address, GPIO.OUT)
        GPIO.setup(self.Control, GPIO.OUT)
        GPIO.setup(self.DataIn, GPIO.IN, GPIO.PUD_UP)

    def read(self):
        vals = [0, 0, 0, 0, 0, 0]

        highList = [[-1],[3],[2],[2,3],[1],[1,3]]

        for i in range(0, 6):
            GPIO.output(self.Control, GPIO.LOW)
            for j in range(0, 4):
                listj = highList[i]
                send = False
                for jlistitem in listj:
                    if jlistitem == j:
                        GPIO.output(self.Address, GPIO.HIGH)
                        send = True
                        break

                if not send:
                    GPIO.output(self.Address, GPIO.LOW)

                vals[i] *= 2

                if GPIO.input(self.DataIn):
                    vals[i] += 1
                GPIO.output(self.Clock, GPIO.HIGH)
                GPIO.output(self.Clock, GPIO.LOW)

            for j in range(0, 6):
                vals[i] *= 2
                if GPIO.input(self.DataIn):
                    vals[i] += 1
                GPIO.output(self.Clock, GPIO.HIGH)
                GPIO.output(self.Clock, GPIO.LOW)

            for j in range(0, 6):
                GPIO.output(self.Clock, GPIO.HIGH)
                GPIO.output(self.Clock, GPIO.LOW)

            GPIO.output(self.Control, GPIO.HIGH)

        for i in range(0, len(vals)):
            n = vals[i]
            if n >= 500:
                vals[i] = 0
            else:
                vals[i] = 1

        return vals[1:]