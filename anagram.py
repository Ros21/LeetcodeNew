"""
2273. Find Resultant Array After Removing Anagrams
"""

class Solution:
    # def is_anagram(self, word1, word2):
    #     map1= {}
    #     for word in word1:
    #         map1[word] = map1.get(word, 0)+1
        
    #     for word in word2:
    #         if word not in map1:
    #             return False
    #         map1[word] = map1.get(word, 0)-1
        
    #     for key, val in map1.items():
    #         if val!=0:
    #             return False
    #     return True

    def remove_anagrams(self, words):
        result = [words[0]]
        for word in words[1:]:
            if sorted(word)!=sorted(result[-1]):
                result.append(word)
        return result


assert Solution().remove_anagrams(["abba","baba","bbaa","cd","cd"])==["abba","cd"]
assert Solution().remove_anagrams(["a","b","c","d","e"])==["a","b","c","d","e"]
assert Solution().remove_anagrams(["a","b","a"])==["a","b","a"]
assert Solution().remove_anagrams(["a","b","b","a"])==["a","b","a"]