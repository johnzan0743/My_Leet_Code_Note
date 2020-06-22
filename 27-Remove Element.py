class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
    
        for i in range(len(nums)):
            if nums[count] == val:
                nums.pop(count)
            else:
                count +=1
        return count
# 注意：此处的count是指length，而不是index，所以return count不需要减一
        
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[count] = nums[i]
#                 count +=1
#         return count
                