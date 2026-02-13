"""
3507. Minimum Pair Removal to Sort Array I
"""
class Solution:
    def minimumPairRemoval(self, nums) -> int:
        def is_sorted(nums):
            for index in range(1, len(nums)):
                if nums[index-1]>nums[index]:
                    return False
            return True


        operation = 0

        while not is_sorted(nums):
            min_sum = float("inf")
            for index in range(1, len(nums)):
                sum = nums[index-1]+nums[index]
                if sum<min_sum:
                    min_sum = min(min_sum,sum)
                    min_index = index-1 
            nums = nums[:min_index]+[min_sum]+nums[min_index+2:]
            operation+=1
        return operation


assert Solution().minimumPairRemoval([5,2,3,1]) == 2
assert Solution().minimumPairRemoval([1,2,2]) == 0
assert Solution().minimumPairRemoval([5,4,3,2,1]) == 4
assert Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]) == 9