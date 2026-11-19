from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # freq = {}
        # maxl = 0

        # for right in range(len(s)):
        #     char = s[right]
        #     freq[char]=freq.get(char,0)+1
        #     while freq[char]>1:
        #         ch = s[left]
        #         freq[ch] -=1
        #         left +=1

        #     maxl = max(maxl, right - left + 1)

        # return maxl







        n = len(s)
        left = 0
        freq = defaultdict(int)
        maxl = 0

        for right in range(n):
            char = s[right]
            freq[char] +=1

            while freq[char]>1:
                ch = s[left]
                freq[ch] -=1
                left +=1

            maxl = max(maxl, right-left+1)
        return maxl


















            
        