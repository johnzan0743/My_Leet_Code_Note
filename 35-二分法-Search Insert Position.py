class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        low = 0
        high = len(nums) -1
        while high > low:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif mid == low:
                return mid+1
            elif target < nums[mid]:
                high = mid
            else:
                low = mid