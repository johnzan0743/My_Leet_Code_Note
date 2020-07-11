class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <=len(nums) and nums[i] != nums[nums[i]-1]:
                # 只取nums[i]为正整数的情况 nums[i]最大可以取到n,即nums里面所有元素均为# 正整数 

                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] 
                # 上一行的交换方法会出错
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # temp = nums[nums[i]-1]
                # nums[nums[i]-1] = nums[i]
                # nums[i] = temp
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1