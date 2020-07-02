class Solution:
    
    def combinationSum(self, candidates, target):
        # import copy
        if not candidates:
            return []
        def dfs(start,candidates,path,result,target):
            if target == 0:
                # result.append(copy.deepcopy(path))
                result.append(path.copy())
                return
            for i in range(start,len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(i,candidates,path,result,target-candidates[i])
                    path.pop()
        result = []
        start = 0
        path = []
        dfs(start,candidates,path,result,target)  
        return result


A = Solution()
candidates = [10,7,5,3,2]
target =15
B = A.combinationSum(candidates, target) 