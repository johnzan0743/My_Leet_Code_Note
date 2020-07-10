class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp_list = []
        result = []
        def backtracking(start, nums, temp_list):
            #result.append(temp_list)  
            #后面不能写return 因为会直接弹出去，无法进入回溯循环
            #如果把result.append写在循环之后，则可以return
            for i in range(start,len(nums)):
                backtracking(i +1,nums,temp_list+[nums[i]])

            result.append(temp_list)
            return result
        backtracking(0,nums,temp_list)