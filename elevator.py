import time
import threading

class Elevator:
    def __init__(self):
        self.numOfPeople = 0
        self.goingUp = False
        self.currFloor = 0
    
    def waitOnFloor():
        pass

    def transition():
        pass

    def isFull(self):
        return (self.numOfPeople == 5)

    def isGoingUp(self):
        return self.goingUp

    def timeToGetToFloor(self, floor):
        if self.currFloor - floor < 0:
            directionNeededIsUp = False
        else: directionNeededIsUp = True
        if directionNeededIsUp != self.goingUp:
            hypotheticalTime+=10
        hypotheticalTime+=(self.currFloor - floor*3)
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

