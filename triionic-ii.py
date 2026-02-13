"""
3640. Trionic Array II
"""
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        p=0

        n=len(nums)
        while p<n-1 and nums[p]<nums[p+1] :
            p+=1
        if p==0:
            return False
        
        q=p
        while q <n-1 and nums[q]>nums[q+1] :
            q+=1     
        if q==p or q==n-1:
            return False
        
        i=q
        while i<n-1 and nums[i]<nums[i+1] :
            i+=1
        if i==q:
            return False
        
        return i==n-1


print(Solution().maxSumTrionic([0,-2,-1,-3,0,2,-1]))  # -4
print(Solution().maxSumTrionic([1,4,2,7]))  # 14

