"""
191. Number of 1 Bits
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            n&=n-1
            count+=1
        return count


print(Solution().hammingWeight(11))  # 3
print(Solution().hammingWeight(128))  # 1
print(Solution().hammingWeight(4294967293))  # 31