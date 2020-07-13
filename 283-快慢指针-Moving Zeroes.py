class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                if count == i:
                    count +=1
                    continue
                # 没必要自己跟自己交换
                else:
                    nums[count], nums[i] = nums[i], nums[count]
                    count +=1