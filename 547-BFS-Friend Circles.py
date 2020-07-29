class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        queue = []
        count = 0
        for i in range(len(M)):
            if i in visited:
                continue
            queue.append(i)
            while queue:
                for j in range(len(queue)):
                    x = queue.pop(0) # 调查x同学的朋友圈情况
                    visited.add(x)
                    for k in range(len(M)):
                        if k not in visited and M[x][k] == 1:
                            queue.append(k)
            count +=1
        return count