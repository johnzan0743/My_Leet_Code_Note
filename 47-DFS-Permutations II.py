class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        result = []
        def dfs(nums,path):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        dfs(nums,path)
        return result