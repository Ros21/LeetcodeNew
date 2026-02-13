"""
2975. Maximum Square Area by Removing Fences From a Field
"""
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences, vFences) -> int:
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        def all_distances(fences):
            distances = set()
            for i in range(0,len(fences)):
                for j in range(i+1,len(fences)):
                    distances.add(fences[j]-fences[i])
            return distances
    
        diff_h = all_distances(h)
        diff_v = all_distances(v)
        common = diff_h.intersection(diff_v)
        if not common:
            return -1
        side = max(common)
        return (side*side)%MOD

        


print(Solution().maximizeSquareArea(m = 4, n = 3, hFences = [2,3], vFences = [2])) # 4
print(Solution().maximizeSquareArea(m = 6, n = 7, hFences = [2], vFences = [4])) # -1
