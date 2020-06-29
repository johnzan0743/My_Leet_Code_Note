class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()

        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                if abs(total-target) < abs(result-target):
                    result = total

                if total < target:
                    l +=1
                elif total > target:
                    r -=1
        return result