import time
import math

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
                
            

class elevatorCar: 
    def __init__(self, upSpeed, downSpeed, pos):
        self.upSpeed = upSpeed
        self.downSpeed = downSpeed
        self.pos = pos
        self.velocity = 0
        self.queue = []
        self.startFloor = pos

    def getVelocity(self):
        return self.velocity

    def getPos(self):
        return self.pos

    def getQueue(self):
        return self.queue

    def setStartFloor(self):
        self.startFloor = self.pos

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
            

    def addToQueue(self, itemToAdd):
        self.queue.append(itemToAdd)
        mySort(self.pos, self.queue)
        elevatorCar.setStartFloor(self)

    def updateVelocity(self):
        if len(self.queue) == 0:
            target = self.pos
        else:
            target = self.queue[0]

        if elevatorCar.roundPos(self) == target:
            self.velocity = 0;
        elif target > self.pos:
            if abs(self.pos-target) <= abs(self.startFloor-target)/5:
                acceleration = -(pow(self.velocity,2)/2*abs(target-self.pos))
            else:
                acceleration = 0.6
                
            if (self.velocity + acceleration/60) >= self.upSpeed:
                self.velocity = self.upSpeed
            else:
                self.velocity += acceleration/60
        elif target < self.pos:
            if abs(self.pos - target) <= abs(self.startFloor-target)/5:
                acceleration = (pow(self.velocity,2)/2*abs(target-self.pos))
            else:
                acceleration = -0.6
                
            if (self.velocity + acceleration/60) <= self.downSpeed:
                self.velocity = self.downSpeed
            else:
                self.velocity += acceleration/60

    def checkDestination(self):
        if len(self.queue) != 0 and self.queue[0] == elevatorCar.roundPos(self) and self.velocity == 0:
            del self.queue[0]
            self.startFloor = self.pos
            time.sleep(5)


    def move(self):
        elevatorCar.updateVelocity(self)
        self.pos += self.velocity/60

    

    


def main():
    carOne = elevatorCar(15, -8, 15)
    elevatorCar.addToQueue(carOne, 30)
    elevatorCar.addToQueue(carOne, 1)

    while True:
        elevatorCar.move(carOne)
        elevatorCar.checkDestination(carOne)
        print(elevatorCar.roundPos(carOne))
        time.sleep(1/60)
        
        


if __name__ == "__main__":
    main()
