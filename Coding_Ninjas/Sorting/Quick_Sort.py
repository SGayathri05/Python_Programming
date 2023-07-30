from typing import List

def partitionArray(input, start, end):
    pivot = input[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= j and input[i] <= pivot:
            i += 1
        while i <= j and input[j] > pivot:
            j -= 1
        if i <= j:
            input[i], input[j] = input[j], input[i]
            i += 1
            j -= 1

    input[start], input[j] = input[j], input[start]
    return j

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as a function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """

    if startIndex < endIndex:
        pindex = partitionArray(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pindex - 1)
        quickSort(arr, pindex + 1, endIndex)
