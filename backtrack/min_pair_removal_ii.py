"""
3510. Minimum Pair Removal to Sort Array II
"""
import heapq


class Solution:
    def minimumPairRemoval(self, nums) -> int:
        n = len(nums)

        # temp array as long[]
        temp = [int(x) for x in nums]

        # doubly-linked list via indices
        nextIndex = [i + 1 for i in range(n)]
        prevIndex = [i - 1 for i in range(n)]

        # min-heap for (sum, idx)
        heap = []

        badPairs = 0
        for i in range(n - 1):
            if temp[i] > temp[i + 1]:
                badPairs += 1
            heapq.heappush(heap, (temp[i] + temp[i + 1], i))

        operations = 0

        while badPairs > 0:
            # lazy removal: ensure pair is still valid
            while True:
                pair_sum, first = heapq.heappop(heap)
                second = nextIndex[first]
                if second < n and pair_sum == temp[first] + temp[second]:
                    break

            first_left = prevIndex[first]
            second_right = nextIndex[second]

            # remove (first, second) bad pair
            if temp[first] > temp[second]:
                badPairs -= 1

            # {d, (a, b)}
            if first_left >= 0:
                if temp[first_left] > temp[first] and \
                   temp[first_left] <= temp[first] + temp[second]:
                    badPairs -= 1
                elif temp[first_left] <= temp[first] and \
                     temp[first_left] > temp[first] + temp[second]:
                    badPairs += 1

            # {(a, b), d}
            if second_right < n:
                if temp[second_right] >= temp[second] and \
                   temp[second_right] < temp[first] + temp[second]:
                    badPairs += 1
                elif temp[second_right] < temp[second] and \
                     temp[second_right] >= temp[first] + temp[second]:
                    badPairs -= 1

            # update heap pairs
            if first_left >= 0:
                heapq.heappush(
                    heap,
                    (temp[first_left] + temp[first] + temp[second], first_left)
                )

            if second_right < n:
                heapq.heappush(
                    heap,
                    (temp[first] + temp[second] + temp[second_right], first)
                )
                prevIndex[second_right] = first

            # merge
            nextIndex[first] = second_right
            temp[first] += temp[second]

            operations += 1

        return operations


print(Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))# == 9
# assert Solution().minimumPairRemoval([1,2,2]) == 0
