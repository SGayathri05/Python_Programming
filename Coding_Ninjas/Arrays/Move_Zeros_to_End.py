def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    n = len(a)
    zero  = []
    non = []
    for i in range(n):
        if (a[i]!=0):
            non.append(a[i])
        else:
            zero.append(a[i])
    res = non+zero
    return res
