class Solution(object): 
    def getRow(self, rowIndex): 
        x = [1] 
        tmp = 1 
        rowIndex += 1 
        
        for i in range(1, rowIndex): 
            tmp = tmp * (rowIndex - i ) / i 
            x.append(tmp) 
        return x
        
#Min:36ms