class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            list_remainder = nums[:i] + nums[i+1:]
            for j in self.permute(list_remainder):
                result.append([nums[i]]+j)
        return result
