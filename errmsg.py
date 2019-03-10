#errormessages
from random import*
messages = ["Die immediately", "Waste of space", "degenerate assmuncher", "error no. 69", ">:(", "hmmm", "I can't believe you've done this", "adAM"]
def getMessage():
    num = randrange(0, len(messages))
    return messages[int(num)]
