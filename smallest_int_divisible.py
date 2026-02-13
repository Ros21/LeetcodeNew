"""
1015. Smallest Integer Divisible by K
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k%5==0:
            return -1

        length =1
        rem = 1 % k 
        while rem != 0:
            rem = (rem*10+1)%k
            length+=1
        return length


assert Solution().smallestRepunitDivByK(1) == 1
assert Solution().smallestRepunitDivByK(2) == -1
assert Solution().smallestRepunitDivByK(3) == 3
assert Solution().smallestRepunitDivByK(5) == -1
assert Solution().smallestRepunitDivByK(6) == -1
assert Solution().smallestRepunitDivByK(7) == 6
assert Solution().smallestRepunitDivByK(23) == 22
