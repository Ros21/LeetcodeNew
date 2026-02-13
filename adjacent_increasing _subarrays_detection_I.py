"""
3349. Adjacent Increasing Subarrays Detection I
"""
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """
        [2,5,7,8,9,2,3,4,3,1,2,3,4,5,6], k=3
        1. loop till end
        2. if count increasing go, decreasing stop
        3. look for adjacent increasing till 
        """
        i = 0
        count = 0
        for num in nums:
            while i<len(nums) and nums[i]<nums[i+1]:
                count+=1
                i=i+1

            


        


assert Solution().hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)==True
# assert Solution().hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)==False
# assert Solution().hasIncreasingSubarrays([1,2,3,4,5],3)==False
# assert Solution().hasIncreasingSubarrays([5,4,3,2,1],2)==False
# assert Solution().hasIncreasingSubarrays([1,2,3,4,5],6)==False
# assert Solution().hasIncreasingSubarrays([1,2,3,4,5],1)==True
# assert Solution().hasIncreasingSubarrays([1,3,2,4,5],3)==False
# assert Solution().hasIncreasingSubarrays([1,2,3,4,5],5)==False



