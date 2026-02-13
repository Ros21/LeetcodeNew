"""
1925. Count Square Sum Triples
"""
import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                s = i*i+j*j
                c = math.isqrt(s)
                if c<=n and c*c==s:
                    count+=2
        return count
            

assert Solution().countTriples(5) == 2
assert Solution().countTriples(10) == 4
