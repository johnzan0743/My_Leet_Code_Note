class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return []
        if len(nums) == 1:
            return 
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return 
        if len(nums) >= 3:
            if list(reversed(nums)) == sorted(nums):
                return nums.sort()
            else:
                for i in range(len(nums)-1,0,-1): #逆序查找 包前不包后
                    if nums[i] <= nums[i-1]:
                        continue
                    else:
                        #nums[i], nums[i-1] = nums[i-1], nums[i]
                        #nums[i:] = sorted(nums[i:])
                        #先排序后交换
                        nums[i:] = sorted(nums[i:])
                        for j in range(i, len(nums)):
                            if nums[i-1] < nums[j]:
                                nums[i-1], nums[j] = nums[j], nums[i-1]
                                break
                        return
        """
        Do not return anything, modify nums in-place instead.
        """
#特例
'''
1,7,9,9,8,3
1,9,7,9,8,3
1,9,3,7,8,9
wrong


1,7,9,9,8,3
1,7,3,8,9,9
1,8,3,7,9,9
right
'''