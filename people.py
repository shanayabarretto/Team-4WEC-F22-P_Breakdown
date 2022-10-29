from datetime import datetime, date, time, timedelta
from os import times
import time

class People:
    def __init__(self, startFloor, endFloor, startTime):
        self.startFloor = startFloor
        self.endFloor = endFloor
        self.startTime = startTime
        self.pickedUp = False
        self.delivered = False

    def floorStart(self):
        return self.startFloor

    def floorEnd(self):
        return self.endFloor


    def personDirection(self):
        if ((self.floorEnd - self.floorStart) > 0):
            direction = 1
        else:
            direction = 0
        return direction

    def Total(self):
        end = datetime.now()
        curr = end.strftime("%H:%M:%S")
        start_t = self.startTime.strftime("%H:%M:%S")
        s_hours = int(start_t.split(':')[0])
        s_minutes = int(start_t.split(':')[1])
        s_seconds = int(start_t.split(':')[2])
        hours = int(curr.split(':')[0])
        minutes = int(curr.split(':')[1])
        seconds = int(curr.split(':')[2])
        before = (s_hours*3600) + (s_minutes*60) + s_seconds
        after  = (hours*3600) + (minutes*60) + seconds
        return after-before







    