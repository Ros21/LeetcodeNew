"""
3340. Check Balanced String
"""
class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_e = 0
        sum_o = 0
        for index in range(len(num)):
            digit = int(num[index])
            if index%2==0:
                sum_e+=digit
            else:
                sum_o+=digit

        return sum_e==sum_o

print(Solution().isBalanced("1234")) #true
# print(Solution().isBalanced("aabbccc")) #false
# print(Solution().isBalanced("")) #true