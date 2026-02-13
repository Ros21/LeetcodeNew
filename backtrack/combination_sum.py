"""
39. Combination Sum
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # i, not i+1, because reuse allowed
                current.pop()

        backtrack(0, [], 0)
        return result



print(Solution().combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]