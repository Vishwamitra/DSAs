def insertionSort(arrayToSort):
    """
    Complexity:
        best    :   O(n)
        average :   O(n^2)
        worst   :   O(n^2)
    parameters:
        arrayToSort : Array to be sorted

    returns:
        sorted array
    """
    for i in range(1, len(arrayToSort)):
        j = i
        while j > 0 and arrayToSort[j] < arrayToSort[j - 1]:
            arrayToSort[j], arrayToSort[j - 1] = arrayToSort[j - 1], arrayToSort[j]
            j -= 1

    return arrayToSort


if __name__ == "__main__":
    array = [2, 5, 1, 5, 8, 9, 0, 10]
    print(insertionSort(array))
