class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Considerations -
        1. Ordinal: the sequence of the array matters as it shows the price for each day - cannot
                    sort or re-arrange array
        '''

        profit, max_profit = 0, 0
        for i in range(len(prices)-1):
            profit = 0
            # print(f'i: {i}')
            for j in range(i+1, len(prices)):
                # print(f'\tj: {j}')
                profit = max(0, prices[j] - prices[i])
                # print(f'profit: {profit}')
                max_profit = max(profit, max_profit)

        return max_profit