from tkinter import *
from errmsg import *
#ELEVATOR PITCH
#elevatorpitch.py
#last modified: 3/10/19
numFloors = 20

root = Tk()
root.minsize(width = 200, height = 300)

floorQueue = []

# FLOOR GOING TO INFO
def gotoFloor (floor):
    floorInterface.set(floor)

def getFloorInfo():
    try:
        entry = int(floorEntry.get())
        addToQueue(entry)
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
    if item not in floorQueue and item <= numFloors:
        print("Big yeet")
        floorQueue.append(item)
        queue.insert(END, item)    
def removeFromQueue():
    if len(floorQueue) > 0:
        del floorQueue[0]
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

queue = Listbox(runtime, listvariable = floorQueue)

def main():
    ## Pack interface
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
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
