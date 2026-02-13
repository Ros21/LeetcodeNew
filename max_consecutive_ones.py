from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        max_count = 0
        k = 2
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            if k<0:
                if nums[left] ==0 :
                    k+=1
                left+=1

            max_count = max(max_count, right-left+1)
        return max_count


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 6
print(Solution().findMaxConsecutiveOnes([0, 0, 0]))  # 2
print(Solution().findMaxConsecutiveOnes([1, 1, 1, 1]))  # 4
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 0, 1]))  # 5
print(Solution().findMaxConsecutiveOnes([]))  # 0   
print(Solution().findMaxConsecutiveOnes([0, 1, 0, 1, 0, 1]))  # 5
print(Solution().findMaxConsecutiveOnes([0, 1, 0, 1, 0, 0, 1, 1]))  # 5
print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 0, 0, 1, 1, 1]))  # 6
