def isCyclicRotation(p: str, q: str) -> int:
    # Write your code here.
    if len(p)==len(q):
        if (p in q+q):
            ans = 1
            return ans
        else:
            ans = 0
            return ans

    
