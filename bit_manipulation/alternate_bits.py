"""
693. Binary Number with Alternating Bits
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=n^(n>>1)
        return x & (x+1)==0
            


print(Solution().hasAlternatingBits(5))  # True
print(Solution().hasAlternatingBits(7))  # False
print(Solution().hasAlternatingBits(11))  # False 1011
print(Solution().hasAlternatingBits(10))  # True
