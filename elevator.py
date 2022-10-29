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

    def timeToGetToFloor():
        pass

    #Mutators
    def addPeople(self, num):
        self.numOfPeople = self.numOfPeople + num

    def removePeople(self, num):
        self.numOfPeople = self.numOfPeople - num

    def changeDirection(self, direction):
        self.goingUp = direction
    
    def changeFloor(self, floorNum):
        self.currFloor = floorNum

