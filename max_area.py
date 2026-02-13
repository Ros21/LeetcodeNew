"""
2943. Maximize Area of Square Hole in Grid
"""
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive_gap(bars):
            bars.sort()
            count = 1
            max_count = 1
            for n in range(1,len(bars)):
                if bars[n]==bars[n-1]+1:
                    count+=1
                    max_count=max(count, max_count)
                else:
                    count = 1
            return max_count + 1


        max_h = max_consecutive_gap(hBars)
        max_v = max_consecutive_gap(vBars)

        side = min(max_h, max_v)
        return side*side


print(Solution().maximizeSquareHoleArea(5, 4, [0,2,4], [0,1,3])) # == 4
print(Solution().maximizeSquareHoleArea(5, 4, [0,1,2,3,4,5], [0,1,2,3,4])) # == 1
print(Solution().maximizeSquareHoleArea(5, 4, [0,3,5], [0,2,4])) # == 9
