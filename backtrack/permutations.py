"""
46. Permutations
"""

class Solution:
    def permute(self, nums):
        result = []
        used = [False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return 

            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False
        backtrack([])
        return result


print(Solution().permute([1,2,3]))











# class Solution:
#     def permute(self, nums):
#         result = []
#         used = [False] * len(nums)

#         def backtrack(path):
#             if len(path) == len(nums):
#                 print(f"path: {path}")
#                 result.append(path[:])
#                 return

#             for i in range(len(nums)):
#                 if not used[i]:
#                     used[i] = True
#                     path.append(nums[i])

#                     backtrack(path)

#                     path.pop()
#                     used[i] = False

#         backtrack([])
#         return result