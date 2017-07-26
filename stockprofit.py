def stock_profit(prices):
    min_stock_price=prices[0]
    max_profit=0
    for price in prices:
        min_stock_price=min(price,min_stock_price)
        comparison_profit=price-min_stock_price
        max_profit=max(comparison_profit,max_profit)
    return max_profit
#print(stock_profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))



def stock_profit2(prices):
    if len(prices) < 2:
        raise Exception("Need at least 2 prices")

    max_profit=prices[1]-prices[0]
    min_stock_price=prices[0]

    for price in prices[1:]:
        comparison_profit=price-min_stock_price
        max_profit=max(max_profit,comparison_profit)
        min_stock_price=min(price,min_stock_price)
    return max_profit



max_profit=stock_profit2([30,22,21,5])
print(max_profit)
