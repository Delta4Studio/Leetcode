class Solution(object): 
    def addDigits(self, num): 
        if (num <=9): 
            return num 
        else: 
            return (num-1) % 9 + 1 
#Min:60ms