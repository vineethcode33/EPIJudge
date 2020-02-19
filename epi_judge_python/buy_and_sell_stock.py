"""5.6 Buy and sell stock to make max profit
Write a program that takes an array denoting the daily stock price, and retums the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.

Hint:ldentifying the minimum and maximum is not enough since the minimum may appear after the maximum
height. Focus on valid differences.

Returns:
    [type] -- [description]
"""


from typing import List
from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    max_profit, min_price_so_far = 0, float("inf")

    for price in prices:
        max_profit_for_the_day = price - min_price_so_far
        max_profit = max(max_profit, max_profit_for_the_day)
        min_price_so_far = min(price, min_price_so_far)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
