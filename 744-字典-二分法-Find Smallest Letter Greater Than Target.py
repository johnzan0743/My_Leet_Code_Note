class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return []
        if len(letters) == 1:
            return letters[0]
        if target >= letters[-1]:
            return letters[0]
        if target < letters[0]:
            return letters[0]
        dic1 = {}
        index = 0
        for letter in letters:
            if letter not in dic1:
                dic1[letter] = index
                index +=1
        keys = list(dic1.keys())
        values = list(dic1.values())
        
        # 巧用keys和values 互换
        p0 = 0
        p1 = values[-1]
        while p1 > p0:
            mid = (p0 + p1)//2
            if keys[mid] == target:
                return keys[mid+1]
            elif p1 - p0 == 1:
                return keys[p1]
            elif keys[mid] > target:
                p1 = mid
            elif keys[mid] < target:
                p0 = mid

作者：johnzan0743
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/solution/qing-xi-hao-yong-de-zi-dian-fa-er-fen-fa-by-johnza/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。