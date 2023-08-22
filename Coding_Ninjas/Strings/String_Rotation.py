def isCyclicRotation(p,q):
    #    Write your code here.
    st = p + p
    if q in st:
        return 1
    return 0
