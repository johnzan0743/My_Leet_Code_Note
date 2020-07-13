class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])  
            # ❌ nums[i] 为当前元素及以前的所有子串中，最大的和 ❌
            # nums[i] 表示的是以当前元素为结尾的子序列中最大的和
            # 即当i=-1时，nums[-1]为当考虑整个数列时，最大有可能的和
            # 即nums[i]包括了所有以nums[i]为结尾的子序列中 和最大的情况
            # 必须加一个全局最大值是因为上面的nums[i]无法考虑nums[3:5]类似这种情况

            
            #这是个迭代的问题
            #举例：最一开始第一个数为nums[1]，那么我们就比较nums[1]与nums[1] + nums[0]谁更大，并把比较大的那个和赋值给nums[1]
            #其实也可以理解为之前所有的元素总和到底是在做正贡献还是负贡献
            #如果是正贡献，那我们就把nums[i]加上，并继续迭代
            #如果是负贡献，则舍弃之前所有的元素之和，从当前元素继续算起
            result = max(result,nums[i])
        return result