class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l]<prices[r]:
                margin = prices[r] - prices[l]
                profit = max(profit, margin)
            else:
                l = r
            r += 1
        
        return profit

s = Solution()

a = s.maxProfit([3,2,4])
print(a)


'''
You are given an array l1 where l1[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: l1 = [7,1,5,3,6,4]
Output: 5

Input: l1 = [7,6,4,3,1]
Output: 0

'''