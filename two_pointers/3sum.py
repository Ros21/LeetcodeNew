"""
15. 3Sum
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue

            low, high = i+1, n-1
            while low<high:
                sum = nums[i] + nums[low] + nums[high]
                if sum==0:
                    result.append([nums[i], nums[low], nums[high]])
                    low+=1
                    high-=1
                    while low<high and  nums[low] == nums[low-1]:
                        low+=1
                    while low<high and  nums[high] == nums[high+1]:
                        high-=1

                elif sum>0:
                    high-=1
                else:
                    low+=1
        return result


assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert Solution().threeSum([]) == []
assert Solution().threeSum([0]) == [] == [] 
assert Solution().threeSum([0,0,0,0]) == [[0,0,0]]
assert Solution().threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]     
