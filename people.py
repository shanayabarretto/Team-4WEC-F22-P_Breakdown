from datetime import datetime, date, time, timedelta
from os import times
import time

class People:
    def __init__(self, startFloor, endFloor, startTime, pickedUp, delivered):
        self.startFloor = startFloor
        self.endFloor = endFloor
        self.startTime = startTime
        self.pickedUp = False
        self.delivered = False

    def floorStart(self):
        return self.startFloor

    def floorEnd(self):
        return self.endFloor

    # not sure what to do for the timing exactly 
    def start(self):
        curr = datetime.now()

    def totalTime(self, timePassed):
        return timePassed - self.startTime

    def timeStart(self):
        return self.startTime







    