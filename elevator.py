import time
import threading
from people import People

class Elevator:
    def __init__(self):
        self.numOfPeople = 0
        self.goingUp = True
        self.currFloor = 0
        self.people = []
        self.queue = []
        self.inMotion = False
    
    def waitOnFloor(self):
        self.inMotion = False
        pass

    def transition(self):
        self.inMotion = True
        pass

    def isFull(self):
        return (self.numOfPeople == 5)

    def isGoingUp(self):
        return self.goingUp

    def timeToGetToFloor(self, data):
        if self.currFloor - data['events'][0]['end'] < 0:
            directionNeededIsUp = False
        else: directionNeededIsUp = True
        if directionNeededIsUp != self.goingUp:
            hypotheticalTime+=10
        hypotheticalTime+=(self.currFloor - data['events'][0]['end'])*3
        # Doesn't include partial floors (ie. 1 out of 3 seconds transition or 5 out 10 seconds at floor)
        return hypotheticalTime

    #Mutators
    def addPeople(self, num):
        self.numOfPeople = self.numOfPeople + num

    def removePeople(self, num):
        self.numOfPeople = self.numOfPeople - num

    def changeDirection(self, direction):
        self.goingUp = direction
    
    def changeFloor(self, floorNum):
        self.currFloor = floorNum

