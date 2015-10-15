class Solution(object):
    def hammingWeight(self, n):
        x = 0
        while n!=0 :
            x += n%2
            n = n>>2
        return x
#Min:44ms