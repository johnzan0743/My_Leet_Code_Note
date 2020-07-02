class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        def dfs(nums, temp):
            if not nums:
                result.append(temp.copy())
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], temp + [nums[i]])
                #temp.append(nums[i])
                #dfs(nums[:i] + nums[i+1:],temp)
                #temp.pop()
        temp = []    
        dfs(nums,temp)
        return result


                     1
                2  3  4  5
            3  4  5
           4,5
           5 4
