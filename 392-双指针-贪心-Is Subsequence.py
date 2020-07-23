class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        if len(s) > len(t):
            return False
        p1 = p2 = 0 # p1->s  p2->t
        for i in range(len(t)):
            if s[p1] == t[p2]:
                p1 +=1
                p2 +=1
                if p1 == len(s):
                    return True
            else:
                p2 +=1
        return False
        