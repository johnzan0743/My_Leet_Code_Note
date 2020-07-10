class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        temp_list = []
        def dfs(start,candidates,target,temp_list):
            if sum(temp_list) == target:
                result.append(temp_list)
                return
                #此处的return是为了回到下面的for循环中
            elif sum(temp_list) > target:
                return
            for i in range(start,len(candidates)):
                if i >start and candidates[i] == candidates[i-1]: 
                    #如果当前的candidates[i]与上一个candidates[i-1]完全相同，则可以跳过一次循环，因为只能之前已经尝试过一次了，而题目要求不要有重复的答案组合
                    continue
                
                if sum(temp_list) < target:
                    dfs(i+1,candidates,target,temp_list+[candidates[i]])
        dfs(0,candidates,target,temp_list)
                    #这里dfs()里面一定要写i+1 而不是start+1, 否则就无法达到去重的效果，因为前面当candidates[i] == candidates[i-1]的时候，continue，这一步就是在去重
        return result






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