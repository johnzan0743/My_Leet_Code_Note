class Solution:
    # 这个题 M[i][j]表示的是i和j是否为朋友关系
    # 对于所有人而言，必有M[i][i] = 1
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        for i in range(len(M)):
            if M[i][i] == 1: # 这一步的判断是为了防止重复访问
                count +=1
                self.dfs(i,M)
        return count
    

    def dfs(self,x,M):
    # dfs的主要作用是把所有是朋友关系的两个人置0
    # 置0有两个作用：1是表示已经拜访过了，2是把他们划到一个圈子里面
        for i in range(len(M)):
            if M[x][i] == 1:
                M[x][i] = M[i][x] = 0
                self.dfs(i,M) 
                # 从x同学出发，可以找到朋友i
                # 这俩人置0之后，再对i同学开启dfs置0