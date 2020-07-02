class Solution:
    def combinationSum2(self, candidates, target):
        #import copy
        candidates.sort()
        result = []

        if not candidates:
            return []
        
        def dfs(temp_list,target,start,result):
            #candidates_left = copy.deepcopy(candidates)
            if sum(temp_list) == target and temp_list not in result:   #注意去重和只能用一次的限制
                result.append(temp_list.copy())
                return
            for i in range(start,len(candidates)):
                if candidates[i] > target:
                    break
                if sum(temp_list + [candidates[i]]) <= target: #and candidates[i] in candidates_left:
                    #candidates_left.remove(candidates[i])
                    temp_list.append(candidates[i])
                    dfs(temp_list,target,i+1,result)
                    temp_list.pop()
        
        temp_list =[]
        dfs(temp_list,target,0,result)
        return result
            
            
        



A = Solution()
candidates = [10,7,5,3,2]
target =15
B = A.combinationSum2(candidates, target)  