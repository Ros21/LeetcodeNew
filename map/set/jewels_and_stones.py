"""
771. Jewels and Stones
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:\
        return sum(stone in jewels for stone in stones)
        # jewels_set = set(jewels)
        # count = 0
        # for stone in stones:
        #     if stone in jewels_set:
        #         count+=1
        # return count


assert Solution().numJewelsInStones("aA", "aAAbbbb")==3
assert Solution().numJewelsInStones("z", "ZZ")==0
assert Solution().numJewelsInStones("z", "ZzZ")==1
assert Solution().numJewelsInStones("z", "zzz")==3
assert Solution().numJewelsInStones("z", "Z")==0
assert Solution().numJewelsInStones("bcd", "abcdeabcd")== 6
assert Solution().numJewelsInStones("xyz", "xxyzzyyzz")== 9
assert Solution().numJewelsInStones("mnop", "mnopqrstuvwxmnop")==8
assert Solution().numJewelsInStones("A", "aAaaAA")==3
assert Solution().numJewelsInStones("", "aAaaAA")==0
assert Solution().numJewelsInStones("aA", "")==0