class Solution(object):
    def maxProfit(self, prices):
        tmp = 0
        sum = 0
        for i in range(0, len(prices)):
            if i!=0 and tmp < prices[i]:
                sum += (prices[i] - tmp)
            tmp = prices[i]
        return sum
#Min:48ms