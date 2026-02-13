"""
1390. Four Divisors
"""
import math
class Solution:
    def sumFourDivisors(self, nums) -> int:
        def divisor_count_sum(num):
            divs = set()
            for i in range(1, int(math.sqrt(num)+1)):
                if num % i ==0:
                    divs.add(i)
                    divs.add(num//i)
            return len(divs),sum(divs)

        total=0
        for num in nums:
            count,sum_d = divisor_count_sum(num)
            if count==4:
                total+=sum_d
        return total


print(Solution().sumFourDivisors([21,4,7])) #32
print(Solution().sumFourDivisors([21,21])) #64
print(Solution().sumFourDivisors([1,2,3,4,5])) #0