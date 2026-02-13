"""
326. Power of Three
"""
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n>=1:
            if n % 3 != 0:
                return False
            n=n/3
        return True
        # if isinstance(math.log(3, 5),int):
        #     return True
        # else:
        #     return False



assert Solution().isPowerOfThree(27)==True
assert Solution().isPowerOfThree(0)==False
assert Solution().isPowerOfThree(9)==True
assert Solution().isPowerOfThree(45)==False
assert Solution().isPowerOfThree(1)==True
assert Solution().isPowerOfThree(2)==False
assert Solution().isPowerOfThree(3)==True
assert Solution().isPowerOfThree(81)==True
assert Solution().isPowerOfThree(82)==False 
assert Solution().isPowerOfThree(-3)==False
assert Solution().isPowerOfThree(243)==True
assert Solution().isPowerOfThree(244)==False    
assert Solution().isPowerOfThree(59049)==True
assert Solution().isPowerOfThree(59050)==False
assert Solution().isPowerOfThree(1162261467)==True
assert Solution().isPowerOfThree(1162261468)==False

"""
27/3 = 9/3 = 3 = 3/3 = 1
30/3=10/3 
45/3=15/3=5/3=1
"""