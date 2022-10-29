from datetime import datetime, date, time, timedelta
from os import times
import time

class People:
    def __init__(self, startFloor, endFloor, startTime):
        self.startFloor = startFloor
        self.endFloor = endFloor
        self.startTime = startTime

    def floorStart(self):
        return self.startFloor

    def floorEnd(self):
        return self.endFloor

    def totalTime(self, timePassed):
        # Pass in the time spent moving in the elevator 
        # and subtract the start time from it
        return timePassed - self.startTime

    def timeStart(self):
        return self.startTime







    