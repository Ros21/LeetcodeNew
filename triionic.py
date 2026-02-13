"""
3637. Trionic Array I
"""
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
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
        
        for i in range(q,n-1):
            if nums[i]>=nums[i+1]:
                return False
            
        return True


print(Solution().isTrionic([1,3,5,4,2,6]))  # True
print(Solution().isTrionic([2,1,3]))  # False
print(Solution().isTrionic([5,9,1,7]))  # True
print(Solution().isTrionic([3,7,1]))  # False
print(Solution().isTrionic([2,4,3,3]))  # False
