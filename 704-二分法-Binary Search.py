class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target > nums[-1] or target < nums[0]:
            return -1
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            mid = (p1+p2)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p1 = mid + 1
            elif nums[mid] > target:
                p2 = mid - 1
        if nums[p1] == target:
            return p1
        else:
            return -1