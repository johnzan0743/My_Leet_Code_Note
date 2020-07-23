class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        nums_2 = nums.copy()
        if not nums:
            return False
        if len(nums) == 1 or len(nums) == 2:
            return True
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                nums.pop(i)
                nums_2.pop(i+1)
                break
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag += 1
                break
        for i in range(len(nums_2)-1):
            if nums_2[i] > nums_2[i+1]:
                flag +=1
                break

        return flag < 2