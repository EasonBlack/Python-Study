class Solution(object):
    def maxProfit(self, prices):
        maxNum = 0
        minNum = 2**32
        for price in prices:
            if price < minNum:
                minNum = price
            else:
                maxNum = max(price - minNum, maxNum)
        return maxNum


a = Solution()
print a.maxProfit([7,1,5,3,6,4])
