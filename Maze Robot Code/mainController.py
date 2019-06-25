from simpleMotor import SimpleMotor
from lineTrackerInterface import TrackerInterface
from algov2 import MazeAlgo
from movementRecorder import MovementRecorder
from learningController import LearningController
from drivingController import DrivingController
import time

'''
Controller to start the basic operation and instanciates the motor and the tracker.
'''
class MainController:
    def __init__(self):
        self.tracker = TrackerInterface()
        self.motor = SimpleMotor(self.tracker)
        self.algo = MazeAlgo()
        self.recorder = MovementRecorder()


    def run(self):
        while not self.tracker.isOnLine():
            time.sleep(1)
        time.sleep(5) #Wait period to remove hand of the robot
        controller1 = LearningController(self.motor,self.tracker)
        controller1.run()
        path = controller1.getPath()
        shortPath = self.algo.process(path)
        print(shortPath)
        time.sleep(60)
        controller2 = DrivingController(shortPath, self.motor)
        while True:
            controller2.run()
            time.sleep(60)


