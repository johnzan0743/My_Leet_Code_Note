class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == 0:
            return [1]
        carry = 0
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
            for i in range(len(digits)-2,-1,-1):
                temp = digits[i]
                digits[i] = (carry+digits[i])%10
                carry = (carry+temp)//10
            if carry == 1:
                return [carry] + digits
            else: return digits
        

        else: return digits[0:len(digits)-1] + [digits[-1]+1]