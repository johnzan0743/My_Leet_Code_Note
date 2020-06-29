import numpy
class Solution:
    def twoSum(self, nums, target):
        dic1 = {}
        origin_index = list(range(len(nums)))
        sorted_index = numpy.argsort(nums)
        nums.sort()
        # dic1 = dict(zip(sorted_index,origin_index))
        for i in range(len(origin_index)):
            dic1[sorted_index[i]] = origin_index[i]
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                result = [i ,j]
                break
            elif sum < target:
                i += 1
            else:
                j -= 1
        actual_index = [sorted_index[i], sorted_index[j]]
        return actual_index