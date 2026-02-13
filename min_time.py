"""
1266. Minimum Time Visiting All Points
"""
class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        total=0
        for index in range(len(points)-1, 0,-1):
            first_point = points[index]
            second_point = points[index-1]
            diff_x = abs(first_point[0]-second_point[0])
            diff_y = abs(first_point[1]-second_point[1])
            total+= max(diff_x,diff_y)
        return total



print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) #7
print(Solution().minTimeToVisitAllPoints([[3,2],[-2,2]])) #5
print(Solution().minTimeToVisitAllPoints([[3,2]])) #0
