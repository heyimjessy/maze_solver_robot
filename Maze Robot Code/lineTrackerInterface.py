from lineTrackerReader import LineTrackerReader

'''
Interface for using the line tracking sensor.
'''

class TrackerInterface:

    def __init__(self):
        self.reader = LineTrackerReader()

    '''
    Checks if the robot is on the black line or not.
    Returns bool
    '''
    def isOnLine(self):
        vals = self.__toCharString__(self.reader.read())
        if vals[2]=='1':
            return True
        else:
            return False

    '''
    Checks if the robot has a left line by checking pattern in substring
    '''
    def hasLeft(self):
        vals = self.__toCharString__(self.reader.read())
        if vals[0:2] == '11':
            return True
        else:
            return False

    '''
    Checks if the robot has a right line by checking pattern in substring
    '''
    def hasRight(self):
        vals = self.__toCharString__(self.reader.read())
        if vals[3:] == '11':
            return True
        else:
            return False

    '''
    Checks if the robot arrived on the finish field by checking pattern in substring
    '''
    def onFinishField(self):
        vals = self.__toCharString__(self.reader.read())
        if vals[1:4] == '111' and vals[0]=='0' and vals[4]=='0':
            return True
        else:
            return False

    '''
    Returns the values of the line sensor
    '''
    def getValues(self):
        return self.__toCharString__(self.reader.read())


    '''
    Converts array into string
    '''
    def __toCharString__(self,v):
        return ''.join(str(e) for e in v)