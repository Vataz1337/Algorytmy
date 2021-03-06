from Tablice.createTables import *
from Sortowania.heapSort import *
from Sortowania.bubbleSort import *
from Sortowania.quickSort import *
from Sortowania.insertionSort import *
import time






def insertionSortWithSorted():
    start = time.time()
    insertionSort(createSorted())
    print("Czas liczenia insert sort z tablica posortowana: ", time.time()-start)
def insertionSortWithRandomlySorted():
    arr = createRandomlySorted()
    start = time.time()
    insertionSort(arr)
    print("Czas liczenia insert sort z tablica w losowym ukladzie: ", time.time() - start)
def insertionSortWithBackwards():
    start = time.time()
    insertionSort(createSortedBackwards())
    print("Czas liczenia insert sort z tablica posortowana od konca: ", time.time() - start)


def bubbleSortWithSorted():
    start = time.time()
    bubbleSort(createSorted())
    print("Czas liczenia bubble sort z tablica posortowana: ", time.time() - start)
def bubbleSortWithRandomlySorted():
    arr = createRandomlySorted()
    start = time.time()
    bubbleSort(arr)
    print("Czas liczenia bubble sort z tablica w losowym ukladzie: ", time.time() - start)
def bubbleSortWithBackwards():
    start = time.time()
    bubbleSort(createSortedBackwards())
    print("Czas liczenia bubble sort z tablica posortowana od konca: ", time.time() - start)


def heapSortWithSorted():
    start = time.time()
    heapSort(createSorted())
    print("Czas liczenia heap sort z tablica posortowana: ", time.time() - start)
def heapSortWithRandomlySorted():
    arr = createRandomlySorted()
    start = time.time()
    heapSort(arr)
    print("Czas liczenia heap sort z tablica w losowym ukladzie: ", time.time() - start)
def heapSortWithBackwards():
    start = time.time()
    heapSort(createSortedBackwards())
    print("Czas liczenia heap sort z tablica posortowana od konca: ", time.time() - start)


def quickSortWithSorted():
    start = time.time()
    n = len(createSorted())
    quickSort(createSorted(), 0, n-1)
    print("Czas liczenia quick sort z tablica posortowana: ", time.time() - start)
def quickSortWithRandomlySorted():
    arr = createRandomlySorted()
    start = time.time()
    n = len(arr)
    quickSort(arr, 0, n-1)
    print("Czas liczenia quick sort z tablica w losowym ukladzie: ", time.time() - start)
def quickSortWithBackwards():
    start = time.time()
    n = len(createSortedBackwards())
    quickSort(createSortedBackwards(), 0, n - 1)
    print("Czas liczenia quick sort z tablica posortowana od konca: ", time.time() - start)

