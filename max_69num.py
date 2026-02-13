class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


print(Solution().maximum69Number(9669))  # Example usage
print(Solution().maximum69Number(9996))  # Example usage
print(Solution().maximum69Number(9999))  # Example usage
print(Solution().maximum69Number(6666))  # Example usage
print(Solution().maximum69Number(6969))  # Example usage
print(Solution().maximum69Number(9696))  # Example usage