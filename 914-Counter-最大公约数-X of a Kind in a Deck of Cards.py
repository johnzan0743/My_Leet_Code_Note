class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter

        set1 = set(Counter(deck).values())

        for i in range(2,min(set1)+1):
            flag = 1
            for x in set1:
                if x%i != 0:
                    flag = 0
                    break
            if flag == 1:
                return True
            #if all(x%i == 0 for x in set1):
                #return True
        return False