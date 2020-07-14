class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 四个指针
        # 第一个指针，i，range(0,n-3) ，实际序号为0到n-4
        # 第二个指针，j，是第一个指针i的下一位 从i+1到n-2
        # 第三个指针，left，是第二个指针j的下一位 永远在第四个右指针的左边，从j+1到n-1
        # 第四个指针，right，是最右指针，从最后一位n往前导，永远比第三个左指针要大
        if not nums or len(nums) < 4:
            return []
        result =  []
        # 所有三指针/四指针遍历，都要考虑是否先给数列排序
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) -1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left + 1 < right and nums[left] == nums[left+1]:
                            left +=1
                        while left < right - 1 and nums[right] == nums[right -1]:
                            right -=1
                        left +=1
                        right -=1
                    elif total < target:
                        left +=1
                    else:
                        right -=1
        return result