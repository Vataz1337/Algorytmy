import random

def createSorted():
    sorted = []
    for i in range(0,500000):
       sorted.append(i)
    return sorted

def createSortedBackwards():
    unsorted = []
    number = 500000
    for i in range(0, 500000):
        number = number-1
        unsorted.append(number)
    return unsorted

def createRandomlySorted():
    sorted = []
    for i in range(0, 100000):
        sorted.append(i)
        random.shuffle(sorted)
    return sorted


print(createRandomlySorted())