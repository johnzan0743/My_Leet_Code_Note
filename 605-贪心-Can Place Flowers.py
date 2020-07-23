class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 以中间的元素为索引，找 '0,0,0' 这种组合
        # 为了避免边界的特判，在两端边界各加一个0
        # 从新list的[1,len(flowerbed)-1]遍历所有元素
        # 如果可以的话，就把0更新成1，并继续遍历
        if n == 0:
            return True
        count = 0
        if not flowerbed:
            return False
        flowerbed = [0] + flowerbed + [0]    
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count +=1
        return count >= n