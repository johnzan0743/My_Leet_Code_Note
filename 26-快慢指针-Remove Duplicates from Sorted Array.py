class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == nums[count]:
                continue
            else:
                count +=1
                nums[count] = nums[i]
        return count + 1