class Solution:
    def threeSum(self, nums):
        result = []
        if not nums:
            return result
        nums.sort()
        if len(nums) < 3:
            return result
        if nums[0] > 0:
            return result
        elif nums[-1] < 0:
            return result
        else:
            for i in range(len(nums)-2):
                if nums[i] + nums[i+1] + nums[i+2] >0:
                    break
                
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                       
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        #if [nums[l],nums[r],nums[i]] not in result:
                        result.append([nums[l],nums[r],nums[i]])
                        while l+1 < r and nums[l] == nums[l+1]:
                            l +=1
                        while r-1 > l and nums[r] == nums[r-1]:
                            r -=1
                        l +=1
                        r -=1
                    
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -=1
                    else: l +=1

                
            return result