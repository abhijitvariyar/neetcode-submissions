class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Considerations -
        1. Ordinal: the sequence of the array matters as it shows the price for each day - cannot
                    sort or re-arrange array
        '''

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                max_profit = max(max_profit, (prices[r]-prices[l]))
            else:
                l = r

            r += 1

        return max_profit