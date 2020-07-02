class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        #注意：此方法中temp是res这个list（即temp_list）的sum，是一个数字，而不是一个list
        def dfs(temp,res):
            nonlocal target
            if temp > target:#剪枝一:当前的总值大于目标值
                return
            if temp == target:#当前值和目标值相等的时候,保存当前结果,并返回
                result.append(res[:])
                return
            for i in candidates:
                if res and res[-1] > i:#防止重复的方法是,不让其找在当前元素以前的元素
                    continue
                dfs(temp + i, res + [i])
        dfs(0, [])
        return result
            

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/combination-sum/solution/pythonti-jie-jian-dan-de-hui-su-fa-by-xiao-xue-66/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。