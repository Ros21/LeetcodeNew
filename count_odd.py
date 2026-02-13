"""
1523. Count Odd Numbers in an Interval Range
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high-low)//2
        if low % 2 == 1 or high % 2 == 1:
            result+=1
        return result

assert Solution().countOdds(3, 7) == 3
assert Solution().countOdds(8, 10) == 1
assert Solution().countOdds(3, 8) == 3 #add 1
assert Solution().countOdds(4, 9) == 3  # add 1 
assert Solution().countOdds(3, 9) == 4  # [3,5,7,9] add +1 in odd
assert Solution().countOdds(4, 10) == 3 # [5,7,9]