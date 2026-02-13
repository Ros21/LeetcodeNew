"""
1518. Water Bottles
"""
class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        # return num_bottles + (num_bottles-1)//(num_exchange-1) # One line solution
        result = num_bottles
        while num_bottles>=num_exchange:
            new_bottles = num_bottles//num_exchange
            result += new_bottles
            remaining = new_bottles + (num_bottles % num_exchange)
            num_bottles = remaining
        return result

assert Solution().numWaterBottles(9, 3) == 13
assert Solution().numWaterBottles(15, 4) == 19
assert Solution().numWaterBottles(5, 5) == 6
assert Solution().numWaterBottles(2, 3) == 2
assert Solution().numWaterBottles(1, 2) == 1
