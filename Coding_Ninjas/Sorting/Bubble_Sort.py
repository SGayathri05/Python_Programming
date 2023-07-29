from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    n = len(arr)
    res = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                res.append(arr[i])
    return res
            
