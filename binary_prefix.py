"""
1018. Binary Prefix Divisible By 5
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        result = []
        for bit in nums:
            curr = curr*2+bit
            result.append(curr%5==0)
        return result
        # def get_decimal(binary_nums):
        #     result = 0
        #     j= 0
        #     for i in range(len(binary_nums)-1,-1,-1):
        #         result = result+binary_nums[i]*pow(10,j)
        #         j=j+1
        #     dec_num = 0
        #     101
        #     1*2+0*2+1*2
        #     i=0
        #     while result:
        #         last_digit = result %10
        #         dec_num+=last_digit*pow(2,i)
        #         result= result//10
        #         i+=1
        #     return dec_num



        # result = []*len(nums)
        # for i in range(1,len(nums)+1):
        #     dec_num = get_decimal(nums[0:i])
        #     print(f"dec_num : {dec_num}")
        #     if dec_num %5==0:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # print(f"result: {result}")
        # return result


assert Solution().prefixesDivBy5([1,0,1]) == [False,False,True]
assert Solution().prefixesDivBy5([0,1,1]) == [True,False,False]
assert Solution().prefixesDivBy5([1,1,1]) == [False,False,False]
assert Solution().prefixesDivBy5([0,1,1,1,1,1]) == [True,False,False,False,True,False]
assert Solution().prefixesDivBy5([1,1,1,0,1]) == [False,False,False,False,False]