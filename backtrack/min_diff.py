"""
1984. Minimum Difference Between Highest and Lowest of K Scores
"""
class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        if k==1:
            return 0
        
        nums.sort()
        min_diff = float("inf")

        for i in range(0,len(nums)+1-k):
            min_diff = min(min_diff, abs(nums[i-1+k]-nums[i]))
        return min_diff 


print(Solution().minimumDifference([90], 1)) #0
print(Solution().minimumDifference([9,4,1,7], 2)) #2
print(Solution().minimumDifference([1,5,6,14,15], 3)) #5
