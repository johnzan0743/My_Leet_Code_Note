class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        final_list = []
        for j in range(len(nums)):
            result = self.findThreeSum(nums[j+1:], target - nums[j])
            for item in result:
                item.append(nums[j])
                item.sort()
                if item not in final_list:
                    final_list.append(item)
        # final_list = [x for x in final_list if x !=[]]
        # result_list = []
        # for x in final_list:
            #     result_list.append(x[0])
        return final_list
    
    
    def findThreeSum(self, nums, target):
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1 
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                elif nums[i] + nums[left] + nums[right] < target:
                    left +=1
                else:
                    right -=1
        return result