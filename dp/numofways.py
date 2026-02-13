"""
1411. Number of Ways to Paint N × 3 Grid
"""
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD= 10**9 + 7
        abc=6
        aba=6
        for _ in range(2,n+1):
            new_a = (2*abc+2*aba) % MOD
            new_b = (2*abc+3*aba) %MOD
            abc = new_a
            aba= new_b
        return (abc+aba)%MOD
        

print(Solution().numOfWays(1))  # 12
print(Solution().numOfWays(2))  # 54
print(Solution().numOfWays(3))  # 246
print(Solution().numOfWays(5000))  # 30228214

