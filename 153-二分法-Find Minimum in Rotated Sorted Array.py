class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            mid = (p1 + p2) //2
            if nums[mid] < nums[p2]:   
            # 此句为关键句！！！整个旋转数组的特点永远是 **相对高点-升序-最低点-升序**
            # 如果此处条件写成 if nums[mid] > nums[p1]
            # 则无法判断如何移动 **因为该题是要寻找最小值
            # 也许最一开始的旋转数组没有问题（当mid大于最左端，则最小值在mid右边），但是当数组被切割成完全单调递增时，最小值变成了在mid左边
            # 所以只能跟最右边比大小，当mid比最右边小时，把p2移动到mid
            # 当mid比最右边大时，移动p1到mid + 1
            # 当我们需要寻找最大值的时候，则跟最左边比较
                p2 = mid
            else:
                p1 = mid + 1
        return nums[p1]