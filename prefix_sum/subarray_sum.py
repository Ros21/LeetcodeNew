"""
560. Subarray Sum Equals K
"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefix_sum = 0
        count_map = {0:1}
        result = 0

        for num in nums:
            prefix_sum += num
            diff = prefix_sum-k
            if diff in count_map:
                result += count_map[diff]
            
            count_map[prefix_sum] = count_map.get(prefix_sum,0)+1
        return result




# assert Solution().subarraySum([1,1,1], 2) == 2
# assert Solution().subarraySum([1,2,3], 3) == 2
# assert Solution().subarraySum([1,2,1,2,1], 3) == 4
assert Solution().subarraySum([1,2,3,-1,2], 3) == 2
# assert Solution().subarraySum([1], 0) == 0
# assert Solution().subarraySum([1,-1,0], 0) == 3
# assert Solution().subarraySum([2,3,-5,5,-5,1,4], 5) == 4