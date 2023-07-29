from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    res = []
    n = len(arr)    
    for i in range(n-1):
        min_val = min(arr[i:])
        min_ind = arr.index(min_val, i) 
        temp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = temp
        res.append(arr[i])
    return res
