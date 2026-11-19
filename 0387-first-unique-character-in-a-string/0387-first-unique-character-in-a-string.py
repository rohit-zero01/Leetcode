class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        freq = Counter(s)

        for i in range(n):
            if freq[s[i]] == 1:
                return i
                break
        return -1
