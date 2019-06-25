#!/home/pi/pyenv/robotenv/bin/python
from mainController import MainController

if __name__ == '__main__':
    '''
    Instanciates the main controller to start the robot
    '''
    prog = MainController()
    prog.run()