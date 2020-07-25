class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 根据题目描述，len(nums)必然为奇数
        # 所以二分之后，找到与nums[mid]相等的那一边
        # 找到之后single element必然在那一边
        
        p1 = 0
        p2 = len(nums) -1
        
        while p2 > p1:
            mid = (p2+p1)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif p2 -p1 == 2:
                if nums[p1] == nums[p1+1]:
                    return nums[p2]
                if nums[p2-1] == nums[p2]:
                    return nums[p1]
            elif nums[mid] == nums[mid-1]:
                if len(nums[p1:mid-1]) % 2 ==0: # 左半边是偶数个，移动p2
                    p1 = mid + 1
                else:
                    p2 = mid -2
            
            elif nums[mid] == nums[mid+1]:
                if len(nums[p1:mid])%2 == 0:
                    p1 = mid + 2
                else:
                    p2 = mid -1
        return nums[p2]