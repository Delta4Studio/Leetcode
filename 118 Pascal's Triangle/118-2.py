class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        x=[[1]]
        if numRows == 1:
            return x
        for I in range(1, numRows):
            x.append([])
            x[i].append(1)
            for j in range(1, i):
                x[i].append(x[i-1][j] + x[i-1][j])
            x[i].append(1)
        return x
#Min:36ms
