class Solution:
    
    def combinationSum(self, candidates, target):
        # import copy
        if not candidates:
            return []
        def dfs(start,candidates,path):
            if sum(path) == target:
                # result.append(copy.deepcopy(path))
                result.append(path)
                return
            if sum(path) > target:
                return 
            for i in range(start,len(candidates)):
                # 此处设置start的唯一作用就只是为了限制candidates的取解空间
                # 当然，它有个连带的好处，就是确保了所求解的唯一性！
                # 每次dfs的时候，取解的空间只能是
                # for i in range(start, len(candidates)):

                # 如果我们能在dfs的输入端设置好新的candidates的范围，则其实可以省略此处的start的设置
                # 不过下面dfs调用的时候，需要改成
                # dfs(candidates[i:],path+[candidates[i]])
                # 由于可以重复取值，所以candidates取解的空间为candidates[i:]
                # 如果不能重复取值（每一个元素只能取一次），那么取解空间就要改成 candidates[i+1:]
                
                # 更改取解的空间，是组合问题的一个重要标志，即取过解的就不要再二次取解了
                # 而排列则不存在这个问题，取解空间通常为candidates[:i]+candidates[i+1:]

                dfs(i,candidates,path+[candidates[i]])

                    # path.append(candidates[i])
                    # dfs(i,candidates,path,result,target-candidates[i])
                    # path.pop()
        result = []
        start = 0
        path = []
        dfs(start,candidates,path)  
        return result


A = Solution()
candidates = [10,7,5,3,2]
target =15
B = A.combinationSum(candidates, target) 