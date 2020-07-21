class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        s.sort()
        g.sort()
        if s[-1] < g[0]:
            return 0
        i = j =0
        total = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                total +=1
                i +=1
                j +=1
            else:
                j +=1
        return total