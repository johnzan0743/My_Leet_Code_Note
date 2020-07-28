class Solution:
    def numSquares(self, n: int) -> int:
        unique_remainder = set()
        upper_bound = int(n**0.5)
        if upper_bound**2 == n:
            return 1
        path = []
        path.append([n,0])
        while path:
            target,step = path.pop(0)
            remainders = [target-i*i for i in range(1,int(target**0.5)+1)]
            if 0 in remainders:
                return step + 1
            else:
                for remainder in remainders:
                    if remainder not in unique_remainder:
                        unique_remainder.add(remainder)
                        path.append([remainder,step+1])