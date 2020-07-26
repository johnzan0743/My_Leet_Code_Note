# 第一种思路：移动mid
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if target > nums[-1] or target < nums[0]:
            return [-1,-1]
        else:
            flag = 0
            left = 0
            right = len(nums) -1
            while left <= right:
                mid = (left+right)//2
                if target == nums[mid]:
                    flag = 1
                    break
                elif target >= nums[left] and target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            if flag == 0:
                return [-1,-1]
            if flag == 1:
                low = mid
                high = mid
                while mid > 0:
                    if nums[mid-1] == nums[mid]:
                        mid -=1
                        low = mid
                    else:
                        break
                while mid < len(nums) -1:
                    if nums[mid+1] == nums[mid]:
                        mid +=1
                        high =mid
                    else:
                        break
                return [low,high]

# 第二种思路，从mid向两边拓展
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        p1 = 0
        p2 = len(nums) - 1
        flag = True
        while p1 < p2:
            mid = (p1+p2)//2
            if nums[mid] < target:
                p1 = mid + 1
            elif nums[mid] > target:
                p2 = mid - 1  # 最后返回p1 
                # 如果nums[mid]一直不与target相等，最终p1和p2会汇合到一个点上
            elif nums[mid] == target:
                flag = False
                break
        if flag is True:
            if nums[p1] == target:
                return [p1,p1]
            else:
                return [-1,-1]
        if flag is False:
            i = 0
            while mid - i >= 0 and nums[mid-i] == nums[mid]:
                i +=1
            low = mid- i + 1
            i = 0
            while mid + i < len(nums)  and nums[mid+i] == nums[mid]:
                i +=1
            high = mid + i - 1
            return [low,high]
                    
        