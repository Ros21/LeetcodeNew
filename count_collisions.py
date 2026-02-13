"""
2211. Count Collisions on a Road
"""
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        result = 0
        i = 0
        while i<n and directions[i]=='L':
            i+=1
        j = n-1
        while j>=0 and directions[j]=='R':
            j-=1
        for k in range(i,j+1):
            if directions[k]!='S':
                result+=1
        return result


assert Solution().countCollisions("RLRSLL") == 5
assert Solution().countCollisions("LLRR") == 0
assert Solution().countCollisions("RRSLL") == 4
assert Solution().countCollisions("RLRLRLRL") == 4
assert Solution().countCollisions("SSSSS") == 0
assert Solution().countCollisions("R") == 0
assert Solution().countCollisions("L") == 0
assert Solution().countCollisions("S") == 0
assert Solution().countCollisions("RS") == 1
assert Solution().countCollisions("SR") == 0
assert Solution().countCollisions("LS") == 1
assert Solution().countCollisions("SL") == 0
assert Solution().countCollisions("RL") == 2
assert Solution().countCollisions("LR") == 0    
assert Solution().countCollisions("RRSRLL") == 4