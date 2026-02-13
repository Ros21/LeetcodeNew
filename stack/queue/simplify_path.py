"""
71. Simplify Path
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        pass


assert Solution().simplifyPath("/home/") == "/home"
assert Solution().simplifyPath("/../") == "/"
assert Solution().simplifyPath("/home//foo/") == "/home/foo"
assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
assert Solution().simplifyPath("/a/../../b/../c//.//") == "/c"
assert Solution().simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
assert Solution().simplifyPath("/...") == "/..."
assert Solution().simplifyPath("/.") == "/"
assert Solution().simplifyPath("/..hidden") == "/..hidden"  
assert Solution().simplifyPath("/a/./b/./c/./d/") == "/a/b/c/d"