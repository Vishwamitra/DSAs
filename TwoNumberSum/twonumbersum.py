
# Solution 1
# Time Complexity = O(n^2)
def twoNumberSum_1(array, targetSum):
    result = []
    for i in range(0, len(array),1):
        for j in range(i+1, len(array), 1):
            if array[i] + array[j] == targetSum:
                result.append(array[i])
                result.append(array[j])
                break
        if result != []:
            break
    return result


# Solution 2 [Best]
# Time Complexity = O(n)
def twoNumberSum_2(array, targetSum):
    for iNum in array:
        expectedNum = targetSum - iNum
        if (expectedNum in array) and (expectedNum is not iNum):
            return [iNum, expectedNum]
    return []