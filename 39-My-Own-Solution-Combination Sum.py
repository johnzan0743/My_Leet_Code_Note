class Solution:
    
    def combinationSum(self, candidates, target):
        # import copy
        '''
        path就是一个temp list，如果多一个分支（元素）还可以满足条件（小于等于target）
        则进行target大小比较判断，如果还是小，那么继续加；
        如果超过了target，则把刚刚最后加入的元素pop出来，继续循环，尝试下一个元素
        直到sum（path）刚好等于target，则把path加入result并return
        否则如果所有剩余元素都不满足条件，则pop掉当前的父类元素
        '''
        if not candidates:
            return []
        def dfs(start,candidates,path,result,target):
            if sum(path) == target:
                # result.append(copy.deepcopy(path))
                result.append(path.copy())
                return
            for i in range(start,len(candidates)):
                if sum(path+[candidates[i]]) <= target:
                    path.append(candidates[i])
                    dfs(i,candidates,path,result,target)
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