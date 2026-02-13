"""
1716. Calculate Money in Leetcode Bank
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        return sum


"""
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is
 (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
 8    9   10  11  12  13  14
 (2 + 3 + 4 + 5 + 6 + 7 + 8) + 
 15   16  17  18  19  20 
 (3 + 4 + 5 + 6 + 7 + 8  ) = 96.
"""



assert Solution().totalMoney(4) == 10
# assert Solution().totalMoney(10) == 37
# assert Solution().totalMoney(20) == 96  
# assert Solution().totalMoney(1) == 1
# assert Solution().totalMoney(7) == 28
# assert Solution().totalMoney(14) == 61
