class Solution:
    def frequencySort(self, s: str) -> str:
        l = list(s)
        c = Counter(l)
        freq = c.most_common()
        ans = []
        for char, count in freq:
            ans.extend([char]*count)

        return "".join(ans)
