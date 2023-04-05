def bubbleSort(arrayToSort):
    """
    Time complexity:
        best    : O(n^2)
        average : O(n^2)
        worst   : O(n^2)
    parameters:
        arrayToSort : Array to be sorted
    returns:
        Sorted array
    """
    size = len(arrayToSort)
    for i in range(size):
        for j in range(0, size - i - 1):
            if arrayToSort[j] > arrayToSort[j + 1]:
                arrayToSort[j], arrayToSort[j + 1] = arrayToSort[j + 1], arrayToSort[j]
    return arrayToSort


def bubbleSortBest(arrayToSort):
    """
    Time complexity:
        best    : O(n) - when array is already sorted
        average : O(n^2)
        worst   : O(n^2)
    parameters:
        arrayToSort : Array to be sorted
    returns:
        Sorted array
    """
    iCount = 0
    isSorted = False
    size = len(arrayToSort)
    while not isSorted:
        isSorted = True
        for i in range(0, size - iCount - 1):
            if arrayToSort[i] > arrayToSort[i + 1]:
                arrayToSort[i], arrayToSort[i + 1] = arrayToSort[i + 1], arrayToSort[i]
                isSorted = False
        iCount += 1
    return arrayToSort
