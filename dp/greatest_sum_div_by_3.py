"""
1262. Greatest Sum Divisible by Three
"""
class Solution:
    def maxSumDivThree(self, nums) -> int:
        total = 0
        rem1=[]
        rem2=[]
        for num in nums:
            total+=num
            if num % 3 == 1:
                rem1.append(num)
            if num % 3 == 2:
                rem2.append(num)
        
        if total%3==0:
            return total
        
        rem1.sort()
        rem2.sort()
        if total % 3 ==1:
            op1 = rem1[0] if rem1 else float('inf')
            op2 = rem2[0]+rem2[1] if len(rem2)>=2 else float('inf')
            return total - min(op1, op2) 

        if total % 3 ==2:
            op1 = rem2[0] if rem2 else float('inf')
            op2 = rem1[0]+rem1[1] if len(rem1)>=2 else float('inf')
            return total - min(op1, op2) 


print(Solution().maxSumDivThree([3,6,5,1,8])) #18