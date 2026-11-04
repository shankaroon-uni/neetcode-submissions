class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        carry = True
        for i in range(len(digits) -1, -1,-1):
            if carry:
                if digits[i] + 1 >9:
                    carry = True
                else:
                    carry = False
                digits[i] = (digits[i]+1)%10
                if i == 0 and carry:
                    return [1] + digits
        return digits