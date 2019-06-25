'''
The movement recorder pushes pre-specified characters in the array, depending on the turnings on the robot
'''
class MovementRecorder:

    def __init__(self):
        self.array = []

    def left(self):
        self.array.append('L')

    def right(self):
        self.array.append('R')

    def back(self):
        self.array.append('B')

    def straight(self):
        self.array.append('S')

    def getArray(self):
        return self.array



