"""
525. Contiguous Array
"""
class Solution:
    def findMaxLength(self, nums) -> int:
        zeros = 0
        ones = 0
        count_diff = {}
        result = 0
        for index, val in enumerate(nums):
            if val==0:
                zeros+=1
            else:
                ones+=1
            diff = ones- zeros
            if diff==0:
                result = max(result, index+1)
            if diff in count_diff:
                result = max(result, index-count_diff[diff])
            else:
                count_diff[diff] = index
        return result

assert Solution().findMaxLength([0,1]) == 2
assert Solution().findMaxLength([0,1,0]) == 2
assert Solution().findMaxLength([0,1,0,1,1,1,0,0]) == 8
assert Solution().findMaxLength([0,1,1,1,1,1,0,0,0]) == 6
