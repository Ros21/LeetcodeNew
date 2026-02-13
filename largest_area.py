"""
3047. Find the Largest Area of Square Inside Two Rectangles
"""
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            for j in range(i+1,n):
                x1_bottom, y1_bottom=bottomLeft[i]
                x1_top, y1_top= topRight[i]
                x2_bottom, y2_bottom =bottomLeft[j]
                x2_top, y2_top= topRight[j]
                overlap_x_bottom = max(x1_bottom,x2_bottom)
                overlap_y_bottom = max(y1_bottom,y2_bottom)
                overlap_x_top = min(x1_top,x2_top)
                overlap_y_top = min(y1_top, y2_top)

                width = overlap_x_top - overlap_x_bottom
                height = overlap_y_top - overlap_y_bottom
                if height>0 and width>0:
                    side = min(height, width)
                    area = side*side
                    max_area = max(area, max_area)
        return max_area


print(Solution().largestSquareArea(bottomLeft = [[1,1],[2,0]], topRight = [[4,2],[7,4]])) # 1
print(Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]])) # 1
print(Solution().largestSquareArea(bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]])) # 4
print(Solution().largestSquareArea(bottomLeft = [[1,1],[3,3],[3,1]],topRight = [[2,2],[4,4],[4,2]])) # 0
   