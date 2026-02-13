"""
3427. Sum of Variable Length Subarrays
"""
class Solution:
    def subarraySum(self, nums) -> int:
        prefix = []
        prefix.append(nums[0])
        for j in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[j])
        subarr= nums[:]
        for i in range(1,len(subarr)):
            start = max(0, i - subarr[i])
            subarr[i] = prefix[i]- prefix[abs(start-1)]
        return sum(subarr)


assert Solution().subarraySum([2,3,1,5]) == 17
# assert Solution().subarraySum([3,1,1,2]) == 13
# assert Solution().subarraySum([4,2,1]) == 10
