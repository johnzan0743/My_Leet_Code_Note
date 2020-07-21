class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(haystack) < len(needle):
            return -1

        p1 = p2 = 0
        sliding_window = []
        while p1 < len(haystack):
            if haystack[p1] == needle[p2]:
                sliding_window.append(p1)
                p1 +=1
                p2 +=1
                if len(sliding_window) == len(needle):
                    return sliding_window[0]
            else:
                if sliding_window:
                    p1 = sliding_window[0]
                    p2 = 0
                    sliding_window = []
                    p1 +=1
                else:
                    p1 +=1
        return -1