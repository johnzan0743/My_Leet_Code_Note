class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort(key= lambda x:(-x[0],x[1]))
        # 因为个子高的人看不到个子矮的人
        # 这句话对于程序而言，就是当个子矮的人在个子高的人的前面的时候，个子高的人的k值不会增加
        # 所以个子高的人的k值是真k值，可以先排好
        # 然后个子矮的人再根据k值插队
        # 某个程度上可以理解成个子高的人的k值比个子矮的人的k值优先度更高
        # 即先根据个子高的人的k值排队
        # 再根据下一个身高的人的k值排队
        #result = [people[0]]
        result = []
        for i in range(len(people)):
            result.insert(people[i][1],people[i])
        return result

# 参考答案讲解
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/