"""
3432. Count Partitions with Even Sum Difference
"""
class Solution:
    def countPartitions(self, nums) -> int:
        total = sum(nums)
        if total % 2 !=0:
            return 0
        else:
            return len(nums)-1


        # total = sum(nums)
        # if total % 2 !=0:
        #     return 0
        # count = 0 
        # for index in range(len(nums)-1):
        #     left_sub_sum = sum(nums[0:index+1])
        #     right_sub_sum = sum(nums[index+1:len(nums)+1 ])
        #     if abs(left_sub_sum -right_sub_sum ) % 2 == 0:
        #         count+=1
        # return count

assert Solution().countPartitions([10,10,3,7,6]) == 4
assert Solution().countPartitions([1,2,2]) == 0
assert Solution().countPartitions([2,4,6,8]) == 3