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
                    
        