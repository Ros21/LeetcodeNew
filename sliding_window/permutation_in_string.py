"""
567. Permutation in String
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        if len_s1>len(s2):
            return False
        for j in range(len(s2)-len_s1+1):
            if "".join(sorted(s1))=="".join(sorted(s2[j:j+len_s1])):
                return True
        return False


assert Solution().checkInclusion("ab", "eidbaooo") == True
assert Solution().checkInclusion("ab", "eidboaoo") == False
assert Solution().checkInclusion("adc", "dcda") == True
assert Solution().checkInclusion("hello", "ooolleoooleh") == False
assert Solution().checkInclusion("a", "ab") == True
assert Solution().checkInclusion("ab", "a") == False