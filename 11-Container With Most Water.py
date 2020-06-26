class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            current_area = (right-left) * min(height[left],height[right])
            result = max(result,current_area)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return result