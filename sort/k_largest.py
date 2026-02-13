"""
1985. Find the Kth Largest Integer in the Array
"""
import heapq
class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, int(num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return str(min_heap[0])
        # k =len(nums)-k
        # def quick_sort(l,r):
        #     pivot = nums[r]
        #     p=l
        #     for i in range(l,r):
        #         if int(nums[i])<int(pivot):
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p+=1
        #     nums[p], nums[r] = nums[r], nums[p]
        #     if p>k:
        #         return quick_sort(l,p-1)
        #     elif p<k:
        #         return quick_sort(p+1,r)
        #     else:
        #         return nums[p]

        # return quick_sort(0, len(nums)-1)
        
assert Solution().kthLargestNumber(["3","6","7","10"], 4) == "3"
assert Solution().kthLargestNumber(["2","21","12","1"], 3) == "2"
assert Solution().kthLargestNumber(["0","0"], 2) == "0"
