"""
744. Find Smallest Letter Greater Than Target
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        # print(f"Start left: {left}, right={right}")
        while left<=right:
            mid=(left+right)//2
            if letters[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return letters[left%len(letters)]

# Example usage
if __name__ == "__main__":  
    solution = Solution()
    print(solution.nextGreatestLetter(["c","f","j"], "a"))  # Output: "c"
    print(solution.nextGreatestLetter(["c","f","j"], "c"))  # Output: "f"
    print(solution.nextGreatestLetter(["x","x","y","y"], "z"))# Output: "x"

