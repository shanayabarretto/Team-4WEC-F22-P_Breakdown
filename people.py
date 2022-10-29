from datetime import datetime, date, time, timedelta
from os import times
import time

class People:
    def __init__(self, startFloor, endFloor, startTime, pickedUp, delivered, direction):
        self.startFloor = startFloor
        self.endFloor = endFloor
        self.startTime = startTime
        self.pickedUp = False
        self.delivered = False
        self.direction = direction

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

    def personDirection(self):
        if ((self.floorEnd - self.floorStart) > 0):
            direction = 1
        else:
            direction = 0







    