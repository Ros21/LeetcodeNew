"""
3707. Equal Score Substrings
"""
class Solution:
    def scoreBalance(self, s: str) -> bool:
        def score(ch):
            return ord(ch)-ord('a')+1

        prefix = 0
        total_score = sum(score(ch) for ch in s)
        
        for ch in s:
            prefix+=score(ch)
            if prefix*2 == total_score:
                return True
        return False


assert Solution().scoreBalance("adcb") == True
assert Solution().scoreBalance("bace") == False