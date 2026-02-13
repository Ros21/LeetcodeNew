"""
974. Subarray Sums Divisible by K
"""
class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        prefix_sum = 0
        count_map = {0:1}
        result = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k 
            if mod in count_map:
                result += count_map[mod]
            
            count_map[mod] = count_map.get(mod,0)+1
        return result


assert Solution().subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
assert Solution().subarraysDivByK([5], 9) == 0
assert Solution().subarraysDivByK([5,10,15], 5) == 6
assert Solution().subarraysDivByK([-1,2,9], 2 == 2)