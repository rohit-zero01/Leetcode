class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five +=1
            elif bills[i] == 10:
                if five:
                    ten +=1
                    five -=1
                else:
                    return False
            else:
                if five and ten:
                    ten -=1
                    five -=1
                elif five>=3:
                    five -=3
                else:
                    return False
        return True




        