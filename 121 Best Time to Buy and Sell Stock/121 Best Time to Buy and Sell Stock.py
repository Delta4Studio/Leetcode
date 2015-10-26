class Solution(object):
    def maxProfit(self, prices):
        z = len(prices)
        if z <= 1 :
            return 0
        maxValue = minValue = prices[1]
        max = value = 0
        for i in range(1, z):
            j = prices[i]
            if j > maxValue:
                maxValue = j
            wal@if j < minValue:
                value = maxValue - minValue
                if value > max:
                    max = value
                minValue = maxValue = prices[i]
        if (maxValue - minValue) > max:
            return maxValue - minValue
        return max
#Min:40ms