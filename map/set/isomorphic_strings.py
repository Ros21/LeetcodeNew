"""
205. Isomorphic Strings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for i,j in zip(s,t):
            if map_s_to_t.get(i,j)!=j or map_t_to_s.get(j,i)!=i:
                return False
            map_s_to_t[i]=j
            map_t_to_s[j]=i
        return True


assert Solution().isIsomorphic("egg", "add")==True
assert Solution().isIsomorphic("foo", "bar")==False
assert Solution().isIsomorphic("paper", "title")==True
assert Solution().isIsomorphic("ab", "aa")==False
assert Solution().isIsomorphic("a", "a")==True
assert Solution().isIsomorphic("a", "b")==True
assert Solution().isIsomorphic("abc", "def")==True
assert Solution().isIsomorphic("abca", "zbxz")==True
assert Solution().isIsomorphic("abca", "zbxy")==False
assert Solution().isIsomorphic("aaaa", "bbbb")==True
assert Solution().isIsomorphic("aaaa", "bbbc")==False
assert Solution().isIsomorphic("abab", "baba")==True