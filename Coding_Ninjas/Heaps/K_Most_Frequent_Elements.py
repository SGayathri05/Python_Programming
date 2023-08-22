from typing import List
from collections import *
def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    c = Counter(arr)
    freq = c.most_common(k)
    res = [k[0] for k in freq]
    return res
