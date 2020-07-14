class Solution:
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        result = []
        temp_list = []
        nums.sort()
        # n = len(nums)
        def dfs(start, nums, temp_list, result, target):
            if len(temp_list) == 4 and sum(temp_list) == target:
                result.append(temp_list)
            if len(temp_list) > 4:
                return
            #if len(temp_list) > 0 and sum(temp_list) > target:
                #return
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(start, nums[i+1:], temp_list+[nums[i]],result, target)
        dfs(0, nums,temp_list,result,target)
        return result

作者：johnzan0743
链接：https://leetcode-cn.com/problems/4sum/solution/si-zhi-zhen-hui-su-suan-fa-dfs-by-johnzan0743/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。