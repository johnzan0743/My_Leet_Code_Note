class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                continue
            elif nums[i] > target:
                return i
        return len(nums)
        