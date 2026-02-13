"""
961. N-Repeated Element in Size 2N Array
"""
class Solution:
    def repeatedNTimes(self, nums) -> int:
        count = {}
        n = len(nums)//2
        for num in nums:
            count[num] = count.get(num,0)+1
            if count[num]== n:
                return num
        print(count)



print(Solution().repeatedNTimes([1,2,3,3])) # 3
print(Solution().repeatedNTimes([2,1,2,5,3,2])) # 2
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4])) # 5