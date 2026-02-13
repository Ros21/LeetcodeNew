"""
3578. Count Partitions With Max-Min Difference at Most K
"""
from collections import deque

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums, k: int) -> int:
        """
        Count partitions into contiguous blocks where each block's (max - min) <= k.
        Returns the count modulo MOD.
        """
        n = len(nums)
        # dp[i] = number of ways to partition first i elements (i from 0..n)
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)  # pref[i] = sum_{t=0..i} dp[t]
        dp[0] = 1
        pref[0] = 1

        minDQ = deque()  # store values (or indices) in increasing order
        maxDQ = deque()  # store values (or indices) in decreasing order

        l = 0  # left pointer of the valid window for current r

        for r in range(n):
            val = nums[r]
            # maintain min deque (increasing)
            while minDQ and minDQ[-1] > val:
                minDQ.pop()
            minDQ.append(val)

            # maintain max deque (decreasing)
            while maxDQ and maxDQ[-1] < val:
                maxDQ.pop()
            maxDQ.append(val)

            # shrink left until window is valid (max - min <= k)
            while maxDQ and minDQ and (maxDQ[0] - minDQ[0] > k):
                # remove nums[l] from deques if they are at the front
                if nums[l] == minDQ[0]:
                    minDQ.popleft()
                if nums[l] == maxDQ[0]:
                    maxDQ.popleft()
                l += 1

            # now every j in [l..r] yields a valid final block j..r
            # dp index shift: dp[r+1] = sum dp[j] for j=l..r
            left_pref = pref[l-1] if l-1 >= 0 else 0
            dp[r+1] = (pref[r] - left_pref) % MOD

            pref[r+1] = (pref[r] + dp[r+1]) % MOD

        return dp[n] % MOD


assert Solution().countPartitions([9,4,1,3,7], 4) == 6
assert Solution().countPartitions([3,3,4], 0) == 2


"""
[9, 4, 1, 3, 7]
[9, 4, 1, 3, 7]
k = 4
"""