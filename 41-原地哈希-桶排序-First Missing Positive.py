class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(len(nums)):
            while 1 <= nums[i] <=len(nums) and nums[i] != nums[nums[i]-1]:
                # 只取nums[i]为正整数的情况 nums[i]最大可以取到n,即nums里面所有元素均为# 正整数
                # 桶排序的目标是达到nums[0] = 1, nums[1] = 2, nums[2] = 3...这么个效# 果，所以当nums[i] 不在正确的位置上时（对于i元素来说，正确的位置为
                # nums[i] - 1），我们就要让这两个元素交换位置。
                # 还有一个隐藏条件就是这两个# 互换的元素不能一样，否则会死循环

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