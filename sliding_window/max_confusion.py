"""
2024. Maximize the Confusion of an Exam
"""
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        max_value = 0
        for right in range(len(answerKey)):
            count[answerKey[right]] = count.get(answerKey[right],0) +1
            max_value = max(count[answerKey[right]],max_value)
            while  (right-left+1)- max_value > k:
                print(f'count here : {count}')
                count[answerKey[left]]-=1
                left+=1
            max_count = max(max_count, right-left+1)
        return max_count



# assert Solution().maxConsecutiveAnswers("TTFF", 2) == 4
# assert Solution().maxConsecutiveAnswers("TFFT", 1) == 3
assert Solution().maxConsecutiveAnswers("TTFTTFTT", 1) == 5

## T T F T T F T T
