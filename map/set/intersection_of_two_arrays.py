"""
350. Intersection of Two Arrays II
"""
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        for num in nums1:
            count1[num] = count1.get(num,0)+1

        result = []
        for num in nums2:
            if num in count1 and count1[num]>0:
                result.append(num)
                count1[num] -= 1
        return result

        # count2 = {}
        # for num in nums2:
        #     count2[num] = count2.get(num,0)+1

        # final_map = {}
        # for key, val in count1.items():
        #     if key in count2:
        #         final_map[key]= min(count1[key], count2[key])

        # result = []
        # for key,val in final_map.items():
        #     result.extend([key]*val)
        
        return result


assert Solution().intersect([1,2,2,1], [2,2])==[2,2]
assert Solution().intersect([4,9,5], [9,4,9,8,4])==[4,9] or [9,4]
assert Solution().intersect([1,2,2,1,3], [2,2,3])==[2,2,3]
assert Solution().intersect([1,2,3], [4,5,6])==[]
assert Solution().intersect([1,1,1,1], [1,1])==[1,1]
assert Solution().intersect([], [1,2,3])==[]
assert Solution().intersect([1,2,3], [])==[]