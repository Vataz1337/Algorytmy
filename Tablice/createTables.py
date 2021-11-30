import random

def createSorted():
    sorted = []
    for i in range(0,500):
       sorted.append(i)
    return sorted

def createSortedBackwards():
    unsorted = []
    number = 500
    for i in range(0, 500):
        number = number-1
        unsorted.append(number)
    return unsorted

def createRandomlySorted():
    randomized = []
    for i in range(0, 500):
        randomized.append(i)
    random.shuffle(randomized)
    return randomized



