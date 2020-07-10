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
                    # 上面三行path.append()...dfs()...path.pop()
                    # 也可以直接写成
                    # dfs(i,candidates,path+[candidates[i]],result,target)
                    # 原因见46题攻略，其实也就是39题V2的答案
                    # 这个题内层dfs的时候target不用减，是因为return的条件设计的是sum(path) == target,而且candidates可以重复使用
                    # 如果return条件设计为if not target，则在内层循环中需要改成target-candidates[i]
        result = []
        start = 0
        path = []
        dfs(start,candidates,path,result,target)  
        return result

# 规范的写法

class Solution:
    def combinationSum(self, candidates, target):
        result = []
        temp_list = []               
        self.dfs(0,candidates,temp_list,target,result)
        return result
    def dfs(self, start, candidates, temp_list, target,result):
        if sum(temp_list) == target:
            result.append(temp_list)
            return
        elif sum(temp_list) > target:
            return
        for i in range(start, len(candidates)):
            if sum(temp_list) < target:
                self.dfs(i, candidates, temp_list+[candidates[i]],target,result)