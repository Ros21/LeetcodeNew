"""
1653. Minimum Deletions to Make String Balanced
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        for ch in s:
            if ch=='b':
                b_count+=1
            else:
                deletions = min(deletions+1, b_count)
        return deletions


print(Solution().minimumDeletions("aababbab")) # ==2
print(Solution().minimumDeletions("bbaaaaabb")) # ==2
print(Solution().minimumDeletions("aaaaabb")) # ==0
print(Solution().minimumDeletions("bba")) # ==1
print(Solution().minimumDeletions("bbaaa")) # ==2
