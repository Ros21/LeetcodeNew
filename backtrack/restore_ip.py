"""
93. Restore IP Addresses
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(path):
            if 
            for ch in s:
                path.append(ch)
                backtrack(path)
                path.pop()

        backtrack([])
        return result


print(Solution().restoreIpAddresses("25525511135")) # ==["255.255.11.135","255.255.111.35"]
print(Solution().restoreIpAddresses("0000")) # ==["0.0.0.0"]
print(Solution().restoreIpAddresses("101023")) # ==["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]