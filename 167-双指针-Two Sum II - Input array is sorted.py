class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return []
        
        left = 0
        right = len(numbers) - 1
        for i in range(len(numbers)):
            while right > left:
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]
                elif numbers[left] + numbers[right] > target:
                    right -=1
                elif numbers[left] + numbers[right] < target:
                    left +=1
                    