class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])  
            #nums[i] 为当前元素及以前的所有子串中，最大的和
            #这是个迭代的问题
            #举例：最一开始第一个数为nums[1]，那么我们就比较nums[1]与nums[1] + nums[0]谁更大，并把比较大的那个和赋值给nums[1]
            #其实也可以理解为之前所有的元素总和到底是在做正贡献还是负贡献
            #如果是正贡献，那我们就把nums[i]加上，并继续迭代
            #如果是负贡献，则舍弃之前所有的元素之和，从当前元素继续算起
            result = max(result,nums[i])
        return result