"""
77. Combinations
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path=[]
        def backtrack(start):
            if len(path)==k:
                result.append(path[:])
                return

            for val in range(start,n+1):
                path.append(val)
                backtrack(val+1)
                path.pop()

        backtrack(1)
        return result


print(Solution().combine(4, 2))  # Expected: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
# print(Solution().combine(1, 1))  # Expected: [[1]]
# print(Solution().combine(5, 3))  # Expected: [[3,4,5],[2,4,5],[2,3,5],[2,3,4],[1,4,5],[1,3,5],[1,3,4],[1,2,5],[1,2,4],[1,2,3]]

