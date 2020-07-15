class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: # 当数组一为空时，直接把数组二复制过来
            nums1[:] = nums2[:]
        nums1_copy = nums1[:m].copy()
        p1 = p2 = 0
        for i in range(m+n):
            if p1 < m and p2 < n: # 这个隐藏条件非常重要，而且很容易被忽略
                if nums1_copy[p1] < nums2[p2]:
                    nums1[i] = nums1_copy[p1]
                    p1 +=1
                else:
                    nums1[i] = nums2[p2]
                    p2 +=1
            # 如果还有剩余的数组
            elif p1 < m and p2 == n:
                nums1[i] = nums1_copy[p1]
                p1 +=1
            elif p1 == m and p2 < n:
                nums1[i] = nums2[p2]
                p2 +=1