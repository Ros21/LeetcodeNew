"""
215. Kth Largest Element in an Array
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quick_sort(l,r):
            pivot = nums[r]
            p = l 
            for i in range(l,r):
                if nums[i]<pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]

            if k>p:
                return quick_sort(p+1,r)
            elif k<p:
                return quick_sort(l,p-1)
            else:
                return nums[p]

        return quick_sort(0,len(nums)-1)

        # can also use heap
        
        # min_heap = []

        # for num in nums:
        #     heapq.heappush(min_heap, num)
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # return min_heap[0]

assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4