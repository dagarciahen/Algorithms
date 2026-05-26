n = int(input())
coins = [1,3, 4]

def dpchange(money):
    m = money
    minNumCoins = [float('inf')]*(money+1)
    minNumCoins[0] = 0
    for m in range(1,m+1):
        for c in coins:
            if m >= c:
                NumCoins = minNumCoins[m-c]+1
                if NumCoins < minNumCoins[m]:
                    minNumCoins[m] = NumCoins
    return minNumCoins[m]

print(dpchange(n))
