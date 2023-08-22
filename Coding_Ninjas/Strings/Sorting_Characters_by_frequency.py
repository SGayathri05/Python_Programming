from collections import *
def sortByFrequency(n: int, s: str) -> str:
    # Write your code here
    l = list(s)
    c = Counter(l)
    freq = c.most_common()
    ans = []
    for char, count in freq:
        ans.extend([char]*count)
    return "".join(ans)

    
