"""
3719. Longest Balanced Subarray I
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        diff_index= {0:-1}
        distinct_even = 0
        distinct_odd = 0
        max_length = 0
        freq = defaultdict(int)

        for i in range(len(nums)):
            if freq[nums[i]]==0:
                if nums[i]%2==0:
                    distinct_even+=1
                else:
                    distinct_odd+=1
            freq[nums[i]]+=1

            diff = distinct_even - distinct_odd
            if diff in diff_index:
                max_length = max(max_length, i-diff_index[diff])
            else:
                diff_index[diff] = i

        return max_length


print(Solution().longestBalanced([2,5,4,3]))  # 4
print(Solution().longestBalanced([3,2,2,5,4]))  # 5
print(Solution().longestBalanced([1,2,3,2]))  # 3
print(Solution().longestBalanced([22,36,22]))  # 1

