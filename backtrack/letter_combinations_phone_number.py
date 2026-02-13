"""
17. Letter Combinations of a Phone Number
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        path = []
        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtrack(index, path):
            if len(path)== len(digits):
                result.append("".join(path[:]))
                return

            for char in phone[digits[index]]:
                path.append(char)
                backtrack(index+1, path)
                path.pop()

        backtrack(0, [])
        return result




print(Solution().letterCombinations("23"))
#["ad","ae","af","bd","be","bf","cd","ce","cf"]