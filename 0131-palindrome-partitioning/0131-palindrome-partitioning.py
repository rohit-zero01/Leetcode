class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def Pal(idx, curr):
            # Your Perfect Base Case: reached the end of the string
            if idx == len(s):
                res.append(list(curr))
                return

            # Scanner 'j' checks all possible cut positions from index 'i' to the end
            for i in range(idx, len(s)):
                # Extract the substring from index i to j
                substring = s[idx : i + 1]
                
                # Check: Is this specific chunk a palindrome?
                if substring == substring[::-1]:
                    # 1. Make the choice
                    curr.append(substring)
                    
                    # 2. Move to the next index right after our cut (j + 1)
                    Pal(i + 1, curr)
                    
                    # 3. Undo the choice (backtrack)
                    curr.pop()

        # Start the recursion at index 0 with an empty current path
        Pal(0, [])
        return res

        # res = []

        # def is_Palindrome(sub):
        #     return sub == sub[::-1]

        # def Pal(idx, curr):
        #     if idx == len(s):
        #         res.append(list(curr))
        #         return

        #     for i in range(idx, len(s)):
        #         if is_Palindrome(s[idx:i+1]):
        #             curr.append(s[idx:i+1])
        #             Pal(i+1, curr)
        #             curr.pop()

        # Pal(0,[])
        # return res

            