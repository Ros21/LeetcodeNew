"""
1588. Sum of All Odd Length Subarrays
"""
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        n = len(arr)
        result = 0

        for i, val in enumerate(arr):
            left = i+1
            right = n-i

            left_even = (left+1)//2
            left_odd = (left)//2

            right_even = (right+1)//2
            right_odd = (right)//2

            odd_count = left_even * right_even + left_odd * right_odd
            result += val*odd_count
        return result


assert Solution().sumOddLengthSubarrays([1,4,2,5,3]) == 58
assert Solution().sumOddLengthSubarrays([1,2]) == 3
assert Solution().sumOddLengthSubarrays([10,11,12]) == 66
assert Solution().sumOddLengthSubarrays([5,9,4,3,8,7,2]) == 216
assert Solution().sumOddLengthSubarrays([1]) == 1