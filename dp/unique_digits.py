"""
357. Count Numbers with Unique Digits
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        # if n==1: return 10
        total = 10
        unique_count = 9
        available = 9
        for k in range(2, n+1):
            unique_count *= available
            total+=unique_count
            available-=1
        return total



print(Solution().countNumbersWithUniqueDigits(3))#91