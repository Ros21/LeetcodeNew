"""
66. Plus One
"""
class Solution:
    def plusOne(self, digits) :
        carry = 0
        for n in range(len(digits)-1, -1,-1):
            if digits[n]<9:
                digits[n]+=1
                return digits
            digits[n]=0
        
        return [1]+digits
        #     digit = digits[n]
        #     if n==len(digits)-1:
        #         carry = 1
        #     digits[n] = (digit+carry)%10
        #     carry = (digit+carry)//10
        # if carry ==1:
        #     digits.insert(0,1)
            
        # print(digits)


print( Solution().plusOne([1, 2, 3]))#==[1, 2, 4]
print(Solution().plusOne([9]))#==[1, 0]
print(Solution().plusOne([1, 9, 9]))#==[2, 0, 0]
