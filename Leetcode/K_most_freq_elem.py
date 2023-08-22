from collections import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = c.most_common(k)
        res = [k[0] for k in freq]
        return res
