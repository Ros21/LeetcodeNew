"""
3713. Longest Balanced Substring I
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        def calculate_max_length(s, ch1, ch2):
            count_1 = 0
            count_2 = 0
            diff_index = {0:-1}
            max_count = 0

            for i in range(len(s)):
                if s[i]!=ch1 and s[i]!=ch2:
                    diff_index = {0: i}
                    count_1 = 0
                    count_2 = 0
                    continue
                
                if s[i]==ch1:
                    count_1+=1
                if s[i]==ch2:
                    count_2+=1

                # if count_1 == count_2:
                #     max_count = max(max_count, count_1 + count_2)

                diff = count_1 - count_2
                if diff in diff_index:
                    max_count = max(max_count, i- diff_index[diff])
                else:
                    diff_index[diff] = i
            return max_count


        #Case-I - max_count contributed by 1 string only
        count=1
        max_count=1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                count=1
            else:
                count+=1
            max_count=max(max_count,count)


        #Case-II - max_count contributed by 2 strings (a,b),(a,c) or (b,c)
        max_count = max(max_count, calculate_max_length(s, 'a','b'))
        max_count = max(max_count, calculate_max_length(s, 'a','c'))
        max_count = max(max_count, calculate_max_length(s, 'b','c'))


        #Case-III - max_count contributed by 3 strings (a,b,c)
        count_a = 0
        count_b = 0
        count_c = 0
        diff_index = {(0,0):-1}

        for i in range(len(s)):
            if s[i]=="a":
                count_a+=1
            elif s[i]=="b":
                count_b+=1
            if s[i]=="c":
                count_c+=1
            
            key = (count_a-count_b, count_a-count_c)
            if key in diff_index:
                max_count = max(max_count, i-diff_index[key])
            else:
                diff_index[key]=i
        
        return max_count







print(Solution().longestBalanced("aaaac")) #4
print(Solution().longestBalanced("aaa")) #3
print(Solution().longestBalanced("abbbbc")) #4
print(Solution().longestBalanced("aaaaaaaaacccccccbccccc")) #14
print("-------")

print(Solution().longestBalanced("abbac")) #4
print(Solution().longestBalanced("abababc")) #6
print(Solution().longestBalanced("aaaabbbbac")) #8
print(Solution().longestBalanced("aaaccc")) #6
print(Solution().longestBalanced("aabcbcbcbc")) #8
print("-------")

print(Solution().longestBalanced("aabbcc")) #6
print(Solution().longestBalanced("abc")) #3
print(Solution().longestBalanced("abcabccba")) #9
print(Solution().longestBalanced("abcbaccba")) #9
print(Solution().longestBalanced("abcbaccbaaaabc")) #9