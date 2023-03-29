
def mergeSort(array, asc=True):
    '''
    Time complexity : O(nlog(n)))
    parameters:
        array   : Array of numbers to be sorted
        asc     : boolean flag to sort ascending
                  descending. Default = True (ascending)
    '''
    midIdx = len(array) // 2
   
    if len(array) == 1:
        return array
    
    leftArr = array[:midIdx]
    rightArr = array[midIdx:]
    # Double recursion
    # 1. To keep on dividing the entire
    #    in half until only one item is left
    #    in both left and right side arrays
    # 2. Each time those sub-arrays will be passed
    #    in the other recursive function, whihc will 
    #    return the sorted sub array.
    return sortArray(mergeSort(leftArr, asc), mergeSort(rightArr, asc), asc)
    
def sortArray(leftArray, rightArray, asc):
    sortedArray = [None] * (len(leftArray) + len(rightArray))
    i=j=k=0
    while i < len(leftArray) and j < len(rightArray):
        # based on ascending or descending order
        if asc:
            if leftArray[i] <= rightArray[j]:
                sortedArray[k] = leftArray[i]
                i += 1
            else :
                sortedArray[k] = rightArray[j]
                j += 1
        else:
            if leftArray[i] >= rightArray[j]:
                sortedArray[k] = leftArray[i]
                i += 1
            else :
                sortedArray[k] = rightArray[j]
                j += 1
        k += 1
    
    while i < len(leftArray):
        sortedArray[k] = leftArray[i]
        i += 1
        k += 1
    while j < len(rightArray):
        sortedArray[k] = rightArray[j]
        j += 1
        k += 1
    
    return sortedArray


if __name__ == "__main__":
    arrayToSort = [4, 6, 1, 10, 8, 9, 50, 7, 56]
    print("Array in ascending order :", mergeSort(arrayToSort))
    print("Array in descending order :", mergeSort(arrayToSort, asc=False))