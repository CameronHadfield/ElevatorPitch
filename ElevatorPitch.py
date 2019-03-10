from tkinter import *
from errmsg import *
from Elevator_Calculations import *
#ELEVATOR PITCH
#elevatorpitch.py
#last modified: 3/10/19
global numFloors
numFloors = 1100000

root = Tk()
root.minsize(width = 200, height = 300)

floorQueue = []
global moving
global stopped
moving = False


# FLOOR GOING TO INFO
def setPos (pos):
    floorInterface.set(pos)

def getFloorInfo():
    try:
        entry = int(floorEntry.get())
        if entry>0 and entry <= numFloors:
            addToQueue(entry)
            elevatorCar.addToQueue(carOne, entry)
    except:
        errorMsg()
        
def setFloors():
    try:
        entry = int(numFloorEntry.get())
        numFloors = entry
        floorInterface.config(from_ = numFloors)
        frameState(setup, False)
        frameState(runtime, True)
    except:
        errorMsg()
        pass

# DISPLAY AN ERROR MESSAGE
def errorMsg():
    #randomize error message
    message = getMessage()
	
    error = Tk()
    error.minsize(width = 200, height = 50)

    errorLabel = Label(error, text = "Errormsg")
    errorLabel.config(text = message)
    errorLabel.pack()
    error.mainloop()

# QUEUE STUFF
def addToQueue(item):
    if item not in floorQueue:
        
        floorQueue.append(item)
        queue.insert(END, item)
        moving = True

        print("Big yeet")
def removeFromQueue(item):
    if len(floorQueue) > 0:
        floorQueue.remove(item)
        queue.delete(0)

# FOR DISABLING FRAMES
def frameState(frame, active):
    for child in frame.winfo_children():
        child.config(state = NORMAL if active else DISABLED)
    
setup = Frame(root)
runtime = Frame(root)
    
numFloorEntry = Entry(setup)
floorEntry = Entry(runtime)
## Numfloors entry
numFloorEntry.insert(0, 'floors????')
numFloorVerify = Button(setup, text = "Captcha", command = setFloors)
    
## Floor Entry
button = Button(runtime, text = "yeeeet", command = getFloorInfo)

## Elevator interface
floorInterface = Scale(runtime, from_= numFloors, to_= 1, resolution = .01)

carOne = elevatorCar(12, -5, 1)


queue = Listbox(runtime, listvariable = carOne.queue)

def moveHandler(motion):
    if not elevatorCar.checkDestination(carOne):
        moving = True
        elevatorCar.move(carOne)
        setPos(carOne.pos)
    elif elevatorCar.checkDestination(carOne) and motion:
        setPos(carOne.queue[0])
        moving = False
        removeFromQueue()
        print("hehe")
        root.update()
        time.sleep(5)
    
def main():
    ## Pack interface
    destination = False
    setup.pack()                    
    numFloorEntry.pack()
    numFloorVerify.pack()
    frameState(setup, True)
        
    runtime.pack()
    floorInterface.pack()
    floorEntry.pack()
    button.pack()
    
    queue.pack()
    frameState(runtime, False)
    moving = False

    while True:
        root.update_idletasks()
        root.update()
        #if moving:
        moveHandler(moving)
        time.sleep(1/60)
        
        

    
    
if __name__ == "__main__":
    main()
