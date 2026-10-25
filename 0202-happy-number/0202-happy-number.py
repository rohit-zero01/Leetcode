# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def getNext(number):
#             total_sum = 0
#             while number > 0:
#                 number, digit = divmod(number, 10)
#                 total_sum += digit ** 2
#             return total_sum

#         slow = n
#         fast = getNext(n)

#         while fast !=1 and slow != fast:
#             slow = getNext(slow)
#             fast = getNext(getNext(fast))
#         return fast == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            
            if n in seen:
                return False
            
            seen.add(n)
            
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return True
        