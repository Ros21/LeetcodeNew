"""
219. Contains Duplicate II
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for index in range(len(nums)):
            if nums[index] in result and abs(result[nums[index]] - index) <= k:
                return True
            result[nums[index]] = index
        return False

assert Solution().containsNearbyDuplicate([1,2,3,1], 3)==True
assert Solution().containsNearbyDuplicate([1,0,1,1], 1)==True
assert Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2)==False
assert Solution().containsNearbyDuplicate([1,2,3,4, 5], 3)==False
assert Solution().containsNearbyDuplicate([1,2,1], 2)==True
assert Solution().containsNearbyDuplicate([1,2,1], 1)==False    