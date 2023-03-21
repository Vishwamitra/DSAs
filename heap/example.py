from minheap import MinimumHeap
from maxheap import MaximumHeap
import math

def tryHeapDataStructure():
    listArrayMin = [100, 2, 3, 4, 7, 9, 10, 8, 16, 14, 20, 21]
    listArrayMax = [100, 2, 3, 4, 7, 9, 10, 8, 16, 14, 20, 21]
    newMinHeap = MinimumHeap(listArrayMin)
    newMaxHeap = MaximumHeap(listArrayMax)


    # print the minimum value i.e. 1
    print(newMinHeap.getMinValue())

    # remove item - It should remove root node - 1
    newMinHeap.remove()

    # now print min value again - 4
    print(newMinHeap.getMinValue())

    # insert another minimum number [1 < 4]
    newMinHeap.insert(1)

    # now print again - It should print 1
    print(newMinHeap.getMinValue())

    # print heapified array in array format
    print(newMinHeap.getHeapArray())

    # print heapified array in tree format
    print(newMinHeap.getHeapTree())
    print(newMaxHeap.getHeapArray())
    print(newMaxHeap.getHeapTree())


if __name__ == "__main__":
    tryHeapDataStructure()