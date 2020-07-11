class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        dic1 = {}
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            else:
                dic1[nums[i]] = nums[i]
        for i in range(1,len(nums)+1):
            if i in dic1:
                continue
            else:
                return i 
        return i + 1. # 如果所有数字都为正整数，则return i+1