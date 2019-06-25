import re

'''
Algorithm class for calculating the shortest path. Using LSRB algorithm to calculate it.
'''
class MazeAlgo:
    #Create the class
    def __init__(self):
        self.last = ''

    #BASE SOURCE OF ALGORITHM: https://www.researchgate.net/publication/311861541_SHORTEST_DISTANCE_MAZE_SOLVING_ROBOT
    #IMPROVED
    #Handles to overall process of the line algorithm
    def process(self,array):
        strFormat = self.__toStringFormat__(array)
        while re.search('LBSBL',strFormat):
            strFormat = self.__phase1__(strFormat)
        strFormat = self.__phase2__(strFormat)
        return self.__toArrayFormat__(strFormat)

    #Replace pattern LBSBL to B
    def __phase1__(self,strFormat):
        while re.search('LBSBL',strFormat):
            strFormat = strFormat.replace('LBSBL','P')
        strFormat = re.sub('[P]{2,}', 'P', strFormat)
        strFormat = strFormat.replace('P','B')
        strFormat = strFormat.replace('BB','B')
        return strFormat

    #Apply LSRB Replacements
    def __phase2__(self,strFormat):
        self.last = strFormat
        while  self.__check__(strFormat):
            # strFormat = re.sub('XXX','N',strFormat,1)
            # LBR=B
            strFormat = re.sub('LBR', 'B', strFormat, 1)
            # RBL=B
            strFormat = re.sub('RBL', 'B', strFormat, 1)
            # SBL=R
            strFormat = re.sub('SBL', 'R', strFormat, 1)
            # LBL=S
            strFormat = re.sub('LBL', 'S', strFormat, 1)
            # RBR=S
            strFormat = re.sub('RBR', 'S', strFormat, 1)
            # SBR=L
            strFormat = re.sub('SBR', 'L', strFormat, 1)
            # LBS=R
            strFormat = re.sub('LBS', 'R', strFormat, 1)
            # RBS=L
            strFormat = re.sub('RBS', 'L', strFormat, 1)
            # SBS=B
            strFormat = re.sub('SBS', 'B', strFormat, 1)
        return strFormat

    '''Make Array into a string'''
    def __toStringFormat__(self,array):
            s = ""
            for item in array:
                s += item
            return s.upper()

    '''Make String into an array'''
    def __toArrayFormat__(self,str):
        a = []
        for s in str:
            a.append(s)
        return a

    '''Check if there is no Bs inside the string'''
    def __check__(self,st):
        if st.endswith('B'):
            raise Exception('Backwards move is invalid on the end. Value: '+st)
        else:
            self.last = st
            return re.search('B',st)