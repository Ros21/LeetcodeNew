"""
347. Top K Frequent Elements
"""
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        min_heap =[]
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [num for freq,num in min_heap]


print(Solution().topKFrequent(nums = [1,2,3,3,3,3,3,4,5], k = 2))