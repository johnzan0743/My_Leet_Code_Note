class Solution:
    def isHappy(self, n: int) -> bool:
        if not n or n <= 0:
            return False
        else:
            seen = []
            total = 0
            flag = self.squareSum(n,seen,total)
            return flag == 1
    def squareSum(self,n,seen,total):
        result = []
        while n > 0:
            temp = n%10
            result.append(temp)
            n = n//10
        for i in result:
            total += i**2
        if total == 1:
            flag = 1
            return flag
        elif total not in seen:
            seen.append(total)
            #n = total
            #total = 0
            return self.squareSum(total,seen,0)
        else:
            flag = 2
            return flag   
# python的一般性递归问题
# 如果一个函数没有确切的return值或者没有return这个指令
# 那么它会的默认return值会是None：NoneType
# 所以在递归中，如果只是在最里层的递归中return了一个数值，那么这个数值是不会传给上一层递归函数的，于是上层的递归函数所return的值全都都会是None。
# 为了避免这种情况的出现，我们需要把整个一层的递归函数return回去，即当我们调用递归函数的时候，当出现新的一层递归时，我们直接return recursion function，即上面第25行所做的事情。

# 当然还有一种设置全局变量的方法，即把需要返回的变量在最一开始初始化一下，
# def __init__(self): self.variable = 0
# 然后直接返回 self.variable
