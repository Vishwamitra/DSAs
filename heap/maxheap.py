import math
class MaximumHeap:
    def __init__(self, array):
        self.heap = self.__buildHeap(array)

    # private methods used within this class
    def __buildHeap(self, array):
        parentNodeIdx = (len(array) - 2) // 2
        for idx in reversed(range(parentNodeIdx + 1)):
            self.__moveDown(array, idx, len(array) - 1)
        return array
       
    def __moveUp(self, heap, startIdx):
        parentIdx = (startIdx - 1) // 2
        while startIdx > 0 and heap[startIdx] > heap[parentIdx]:
            heap[startIdx], heap[parentIdx] = heap[parentIdx], heap[startIdx]
            startIdx = parentIdx
            parentIdx = (startIdx - 1) // 2
    
    def __moveDown(self, heap, startIdx, endIdx):
        childOneIdx = startIdx * 2 + 1
        while childOneIdx <= endIdx:
            if (startIdx * 2 + 2) <= endIdx:
                childTwoIdx = startIdx * 2 + 2
            else:
                childTwoIdx = -1
            if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
                possibleSwapIdx = childTwoIdx
            else:
                possibleSwapIdx = childOneIdx
            if heap[possibleSwapIdx] > heap[startIdx]:
                heap[startIdx], heap[possibleSwapIdx] = heap[possibleSwapIdx], heap[startIdx]
                startIdx = possibleSwapIdx
                childOneIdx = startIdx * 2 + 1
            else:
                return

    # public methods used to add, get and 
    # insert a new item in the heap

    def insert(self, item):
        self.heap.append(item)
        self.__moveUp(self.heap, len(self.heap) - 1)

    def remove(self):
        lastIdx = len(self.heap) - 1
        self.heap[0], self.heap[lastIdx] = self.heap[lastIdx], self.heap[0]
        self.heap.pop()
        self.__moveDown(self.heap, 0, len(self.heap) - 1)
    
    # returns heapified array
    def getHeapArray(self):
        return self.heap

    # print heapified array in tree structure
    def getHeapTree(self):
        k = level = 0
        tree = ""
        size = len(self.heap) - 1
        lSize = int(math.floor(math.log(16, 2))) + 1
        totalSpace = (2**lSize)*2
        while k <= size:
            levelMax = 2**level
            for l in range(1, levelMax+1):
                tree = tree + " "*int(totalSpace/(2**level + 1)) + str(self.heap[k])
                k = k + 1
                if k > size:
                    break
            level += 1
            tree = tree + "\n\n"
        return tree

    # returns minimum value
    def getMinValue(self):
        return self.heap[0]