"""
904. Fruit Into Baskets
"""
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,total = 0,0
        count = {}
        max_count = 0 
        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count)>2:
                print(count)
                count[fruits[left]]-=1

                if count[fruits[left]]==0:
                    count.pop(fruits[left])
                left+=1
            max_count = max(max_count, right-left+1)
        return max_count


assert Solution().totalFruit([1,2,1]) == 3
assert Solution().totalFruit([0,1,2,2]) == 3
assert Solution().totalFruit([1,2,3,2,2]) == 4
assert Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
assert Solution().totalFruit([1,0,1,4,1,4,1,2,3]) == 5