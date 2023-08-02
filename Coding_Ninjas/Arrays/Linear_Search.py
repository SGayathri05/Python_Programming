def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return i
    return -1
