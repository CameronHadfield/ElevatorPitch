#errormessages
from random import*
messages = ["Die immediately", "Waste of space", ">>>:(", "error no. 69", ">:(", "hmmm", "I can't believe you've done this", "Please stop I need to feed my family", "JUST DO SOMETHING RIGHT", "Me and your mother are very disappointed in you"]
def getMessage():
    num = randrange(0, len(messages))
    return messages[int(num)]
