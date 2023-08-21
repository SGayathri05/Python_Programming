class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = [s.index(i) for i in s]
        m2 = [t.index(i)for i in t]
        return m1==m2
