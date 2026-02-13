
"""
523. Continuous Subarray Sum
"""
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        prefix = 0
        modulus_count = {}
        for index, val in enumerate(nums):
            prefix+=val
            modu = prefix % k 

            if modu == 0 and index>=1:
                return True

            if modu in modulus_count:
                if index-modulus_count[modu]>=2:
                    return True
            else:
                modulus_count[modu] = index
        return False



# assert Solution().checkSubarraySum([23,2,4,6,7], 6) == True
# assert Solution().checkSubarraySum([23,2,6,4,7], 6) == True
# assert Solution().checkSubarraySum([23,2,6,4,7], 13) == False
assert Solution().checkSubarraySum([23,2,4,6,6], 7) == True
