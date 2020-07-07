class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        if len(nums) == 1:
            return True
        max_distance = nums[0]
        for i in range(len(nums)-1): #不包括最后一位，从第一位开始遍历
            if i <= max_distance:  #i表示所在的index，如果该index小于等于max_distance，则说明已经被之前的cover了
                max_distance = max(max_distance,i+nums[i])
            else:
                break
        return max_distance >= len(nums) - 1 #判断是否能够cover到最后一位的index
            
    

# [0], 2, [0,1,2]
# [1], 3, [1,2,3,4]
# [2], 1, [2,3]
# [3], 1, [3,4]


# [0], 3, [0,1,2,3]
# [1], 2, [1,2,3]
# [2], 1, [2,3]
# [3], 0, [3]