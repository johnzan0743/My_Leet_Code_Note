# sort法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        return nums[k-1]

# heap法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_element = heapq.nlargest(k, nums)[-1]
        return kth_element

# 快排法 quicksort
