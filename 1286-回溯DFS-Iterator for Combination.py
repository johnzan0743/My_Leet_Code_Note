class Solution:
    def __init__(self,characters,combinationLength): # 括号里面的是所有user input
        self.characters = characters
        # 字典序 本身characters就是不含重复的字典序字符串
        self.combinationLength = combinationLength # self.xxx是整个class的全局变量
        self.result = []
        self.count = 0
        self.dfs('',self.characters)   # 运行dfs，获得所有可能的组合
    
    def dfs(self,path,candidates):
        if len(path) == self.combinationLength:
            self.result.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(path+candidates[i],candidates[i+1:]) # 所有字母只能取一次
    
    def next(self):
        self.count +=1
        return self.result[self.count-1]
    
    def hasNext(self):
        return self.count < len(self.result)
