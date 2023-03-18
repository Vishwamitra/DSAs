from minheap import MinimumHeap

def tryHeapDataStructure():
    listArray = [19, 99, 20, 3, 4, 10, 18]
    newHeap = MinimumHeap(listArray)

    # print the minimum value i.e. 3
    print(newHeap.getMinValue())

    # remove item - It should remove root node - 3
    newHeap.remove()

    # now print min value again - 4
    print(newHeap.getMinValue())

    # insert another minimum number [1 < 4]
    newHeap.insert(1)

    # now print again - It should print 1
    print(newHeap.getMinValue())

if __name__ == "__main__":
    tryHeapDataStructure()