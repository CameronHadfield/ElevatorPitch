"""
Performs calculations for the physics of an elevator which prioritizes
moving to the furthest floor in the queue

Author: Calum Offer
Date Created: March 10 2019
Date Last Modified: March 10 2019
"""
#Imports
import time
import math

# Sorts an inputted list from furthest from inputted bound to closest to inputted bound
def mySort(bound, listToSort):
    for index in range(1,len(listToSort)):
        value = listToSort[index]
        i = index - 1
        while i>=0:
            if abs(bound-value) < abs(bound-listToSort[i]):
                listToSort[i+1] = listToSort[i]
                listToSort[i] = value
                i = i - 1
            else:
                break

# Elevator car class used to simulate a single elevator car
class elevatorCar:
    # Constructor Method
    def __init__(self, upSpeed, downSpeed, pos):
        self.upSpeed = upSpeed
        self.downSpeed = downSpeed
        self.pos = pos
        self.velocity = 0
        self.queue = []
        self.startFloor = pos

    # Rounds the closest position to an integer. The rounding is dependent on
    # which direction the car is moving
    def roundPos(self):
        if self.velocity >= 0:
            if abs(math.ceil(self.pos) - self.pos) <= 0.2:
                return math.ceil(self.pos)
            else:
                return math.floor(self.pos)
        else:
            if abs(math.floor(self.pos) - self.pos) <= 0.2:
                return math.floor(self.pos)
            else:
                return math.ceil(self.pos)
            

    # Adds a specified element to the elevator car queue. Causes the elevator car to
    # resort the queue
    def addToQueue(self, itemToAdd):
        self.queue.append(itemToAdd)
        mySort(self.pos, self.queue)
        self.startFloor = self.pos

    # Updates the car's velocity depending on which floor is first in the queue
    def updateVelocity(self):
        if len(self.queue) == 0:
            target = self.pos
        else:
            target = self.queue[0]

        if elevatorCar.roundPos(self) == target:
            self.velocity = 0;
        elif target > self.pos:
            if abs(self.pos-target) <= abs(self.startFloor-target)/2:
                acceleration = -0.6
            else:
                acceleration = 0.6
                
            if (self.velocity + acceleration/60) >= self.upSpeed:
                self.velocity = self.upSpeed
            else:
                self.velocity += acceleration/60
        elif target < self.pos:
            if abs(self.pos - target) <= abs(self.startFloor-target)/2:
                acceleration = 0.6
            else:
                acceleration = -0.6
                
            if (self.velocity + acceleration/60) <= self.downSpeed:
                self.velocity = self.downSpeed
            else:
                self.velocity += acceleration/60

    # Checks if the car is within distance of the first item in queue.
    # Stops at the floor if it is within the distance
    def checkDestination(self):
        if len(self.queue) != 0 and self.queue[0] == elevatorCar.roundPos(self) and self.velocity == 0:
            del self.queue[0]
            self.startFloor = self.pos
            return true
        else:
            return false

    # Moves the elevator car and checks if it has arrived at the target floor
    def move(self):
        elevatorCar.updateVelocity(self)
        self.pos += self.velocity/60
        elevatorCar.checkDestination(self)
