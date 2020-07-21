class Solution:
    def combinationSum2(self, candidates, target):
        # 因为所有元素只能用一次，在有重复元素的情况下，需要提前对原数组进行排序
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider it as a solution, and stop there
        # 当target为0时，target为假，not target为真，把path(即temp_list)加入到result list里面
        if not target: 
            result.append(path)
            return

        for i in range(start, len(nums)):
            '''
            Very important here! We don't use `i > 0` because we always want 
            to count the first element in this recursive step even if it is the same as one before. To avoid overcounting, we just ignore the duplicates after the first element.
            '''
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # 因为元素不能重复拿取，所以寻找下一个搭配对象的元素必须从i+1开始找起
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])
# 上面是有start来限定取解空间的解法
# 下面附上根据我自己的理解，通过更改每次循环candidates的取值范围，而省略start参数的解法
# 记得最开始要对原数列排序，因为每一个元素都只能取一次
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        candidates.sort()
        def dfs(candidates,path):
            if sum(path) == target:
                result.append(path)
                return
            if sum(path) > target:
                return 
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates[i+1:],path+[candidates[i]])
        dfs(candidates,path)
        return result