"""
215. Kth Largest Element in an Array
"""
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            print(min_heap)
            heapq.heappush(min_heap, num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        return min_heap[0]


print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))  #5
