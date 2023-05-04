def heapSorting(array):

    """
    Complexity:
        best    :   O(n log(n))
        average :   O(n log(n))
        worst   :   O(n log(n))
    parameters:
        arrayToSort : Array to be sorted

    returns:
        sorted array
    """

    buildHeap(array)
    for idx in reversed(range(1, len(array))):
        array[0], array[idx] = array[idx], array[0]
        moveDown(array, 0, idx - 1)
    return array


# to build the heap at first
# later by shifting down and
# popping out first item, sorted
# array will be formed
def buildHeap(array):
    parentNodeIdx = (len(array) - 2) // 2
    for idx in reversed(range(parentNodeIdx + 1)):
        moveDown(array, idx, len(array) - 1)


# this is to move down after popping out
# first item
def moveDown(heap, startIdx, endIdx):
    childOneIdx = startIdx * 2 + 1
    while childOneIdx <= endIdx:
        if (startIdx * 2 + 2) <= endIdx:
            childTwoIdx = startIdx * 2 + 2
        else:
            childTwoIdx = -1
        if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
            possibleSwapIdx = childTwoIdx
        else:
            possibleSwapIdx = childOneIdx
        if heap[possibleSwapIdx] < heap[startIdx]:
            heap[startIdx], heap[possibleSwapIdx] = (
                heap[possibleSwapIdx],
                heap[startIdx],
            )
            startIdx = possibleSwapIdx
            childOneIdx = startIdx * 2 + 1
        else:
            return


if __name__ == "__main__":
    array = [2, 5, 1, 5, 8, 9, 0, 10]
    print(heapSorting(array))
