class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: #寻找有序数列->左半边为有序数列
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid +1
            elif nums[mid] <= nums[right]: #右边序列为升序序列
                if target > nums[mid] and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1
'''
这个题的核心问题是找到升序数列
通过那一段升序数列来判断target是否在升序数列
如果target在升序数列的范围内，则说明应该取升序序列继续做二分
如果target不在升序数列范围内，则说明应该取无序序列继续做二分
'''