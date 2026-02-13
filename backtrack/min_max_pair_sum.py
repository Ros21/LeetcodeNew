"""
1877. Minimize Maximum Pair Sum in Array
"""
class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        print(nums)
        left = 0
        right = len(nums)-1
        max_sum = float("-inf")
        for i in range(len(nums)//2):
            sum = nums[left]+nums[right]
            max_sum = max(max_sum, sum)
            left += 1
            right -= 1
        return max_sum



print(Solution().minPairSum([3,5,2,3])) #7
print(Solution().minPairSum([3,5,4,2,4,6])) #8
print(Solution().minPairSum([4,1,5,1,2,5,1,5,5,4])) #8