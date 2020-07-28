class Solution:
    def __init__(self):
        self.result = float('inf')
    def numSquares(self, n: int) -> int:
        upper_bound = int(n**0.5)
        if upper_bound**2 == n:
            return 1
        #candidates = list(map(lambda x:x*x,[i for i in range(upper_bound,0,-1)]))
        candidates = [i*i for i in range(upper_bound,0,-1)]
        path = []
        
        self.dfs(candidates,path,n)
        return self.result
    
    def dfs(self,candidates,path,n):

        for i in range(len(candidates)):
            if sum(path) == n:
                self.result = min(self.result,len(path))
                return
            if sum(path) > n:
                return
            if sum(path) < n:
                self.dfs(candidates[i:],path+[candidates[i]],n)
