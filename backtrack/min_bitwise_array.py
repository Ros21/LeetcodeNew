"""
3315. Construct the Minimum Bitwise Array II
"""
class Solution:
    def minBitwiseArray(self, nums):
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                print(res,d)
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums
    

print(Solution().minBitwiseArray([7]))#  == [-1,1,4,3]
# print(Solution().minBitwiseArray([11,13,31]))#  == [9,12,15]