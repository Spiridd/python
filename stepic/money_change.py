n = int(input())
# coins = [25, 10, 5, 2, 1]
coins = (25, 10, 1)
quantities = []
for coin in coins:
    q = n//coin
    quantities.append(q)
    n -= q*coin
print('%d coins' % sum(quantities))
[print(coins[i], 'x', quantities[i]) for i in range(len(coins))]
