class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
    
        for i in range(len(nums)):
            if nums[count] == val:
                nums.pop(count)
            else:
                count +=1
        return count
# 注意：此处的count是指length，而不是index，所以return count不需要减一

#双指针 
'''
跟方法一类似，这里也要注意，position指的是index而非length
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position = len(nums) -1
        i = 0
        while i <= position:
            if nums[i] == val:
                nums[i], nums[position] = nums[position], nums[i]
                position -=1
            else:
                i +=1
        return position +1
                


#暴力法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val)>0:
            nums.remove(val)
        return len(nums)


                