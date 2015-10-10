class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        x=[[1]]
        if numRows == 1:
            return x
        for i in range(1, numRows):
            x.append([])
            x[i].append(1)
            for j in range(1, i):
                x[i].append(x[i][j-1] * (i+1-j) / j )
            x[i].append(1)
        return x
#Min:40ms
