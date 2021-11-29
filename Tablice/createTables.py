import random

def createSorted():
    sorted = []
    for i in range(0,200):
       sorted.append(i)
    return sorted

def createSortedBackwards():
    unsorted = []
    number = 200
    for i in range(0, 200):
        number = number-1
        unsorted.append(number)
    return unsorted

def createRandomlySorted():
    randomized = []
    for i in range(0, 200):
        randomized.append(i)
    random.shuffle(randomized)
    return randomized



