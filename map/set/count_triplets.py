"""
3583. Count Special Triplets
"""
class Solution:
    def specialTriplets(self, nums) -> int:
        index_map = {}
        count = 0
        for index,num in enumerate(nums):
            if num in index_map and num//2 in index_map:
                num_pos = index_map.get(num//2)
                if index_map.get(num) < num_pos < index :
                    count+=1
            else:
                index_map[num] = index

        print(index_map)
        print(count)
        return count



# assert Solution().specialTriplets([6,3,6]) == 1
assert Solution().specialTriplets([0,1,0,0]) == 1
# assert Solution().specialTriplets([8,4,2,8,4]) == 2