"""
696. Count Binary Substrings
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        result = 0
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else:
                result+=min(curr,prev)
                prev = curr
                curr=1
        result+=min(curr,prev)
        return result
    

print(Solution().countBinarySubstrings("00110011"))  # 6
print(Solution().countBinarySubstrings("10101"))  # 4   
print(Solution().countBinarySubstrings("00110"))  # 3
print(Solution().countBinarySubstrings("10100"))  # 3