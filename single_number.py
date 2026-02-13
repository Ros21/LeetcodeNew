"""
136. Single Number
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count= {}
        res = 0
        for num in nums:
            res^=num
        return res
        #     count[num]= count.get(num,0)+1
        
        # for key,val in count.items():
        #     if val!=2:
        #         return key



assert Solution().singleNumber([2,2,1])==1
assert Solution().singleNumber([4,1,2,1,2])==4
assert Solution().singleNumber([1])==1
assert Solution().singleNumber([0,1,0])==1
assert Solution().singleNumber([-1,-1,-2])==-2
assert Solution().singleNumber([10,9,10,9,8])==8

