class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start,end = 0, 0

        def f(left, right):
            while left>=0 and right < n and s[left]==s[right]:
                left -=1
                right +=1
            return left +1, right -1
            

        for i in range(n):
            l1, r1 = f(i,i)
            l2, r2 = f(i, i+1)

            if r1- l1 > end - start:
                start , end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start: end+1]

       












        
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         start, end = 0, 0

#         def expand_from_center(left: int, right: int) -> tuple[int, int]:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             # Step back to the last valid palindromic indices
#             return left + 1, right - 1

#         for i in range(len(s)):
#             # Odd-length palindromes (single character center)
#             l1, r1 = expand_from_center(i, i)
#             # Even-length palindromes (center between i and i + 1)
#             l2, r2 = expand_from_center(i, i + 1)

#             if r1 - l1 > end - start:
#                 start, end = l1, r1
#             if r2 - l2 > end - start:
#                 start, end = l2, r2

#         return s[start : end + 1]