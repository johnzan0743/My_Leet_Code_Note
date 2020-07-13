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


                      1     2     3     4     5
                2  3  4  5
            3  4  5
           4,5
           5 4


'''
第二种思路
'''
class Solution:
    def permute(self, nums):
        temp = []
        result = []
        n = len(nums)
        self.dfs(temp,nums,result,n)
        return result
    def dfs(self,temp,nums,result,n):
        if len(temp) == n:
            result.append(temp)
            return
        for i in range(len(nums)):
            self.dfs(temp+[nums[i]], nums[:i]+nums[i+1:],result,n)
            # 因为下面self.dfs()中已经把nums[i]去掉了，所以循环的时候直接
            # for i in range(len(nums))就可以了，括号里的nums已经把nums[i]去掉了

A =Solution()
nums = [1,2,3]
B= A.permute(nums)

'''
backtracking中return的作用为返回上一层，并把最后加入temp_list的元素pop出来
因为是通过“temp_list + [nums[i]]”在dfs嵌套，所以dfs每return一次，就会甩掉
一个nums[i]
当然了，满足条件时：
                result.append(temp_list)
            return
也有返回上一层的作用，也可以吧temp_list的元素pop出来
'''