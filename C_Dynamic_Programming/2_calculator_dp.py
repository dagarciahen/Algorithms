n = int(input())

def calculator(n):
    dp = [0]*(n+1)
    parent = [0]*(n+1)

    dp[0] = 0
    dp[1] = 1
    parent[0] = 0
    parent[1] = 0

    for i in range(2, n+1):
        dp[i] = dp[i-1] +1
        parent[i] = i-1

        if i % 2 == 0:
            if dp[i//2] +1 < dp[i]:
                dp[i] = dp[i//2] + 1
                parent[i] = i //2
        if i % 3 == 0:
            if dp[i//3] + 1 < dp[i]:
                dp[i] = dp[i//3] +1
                parent[i] = i//3

    sequence = []
    curr = n
    while curr > 0:
        sequence.append(curr)
        curr = parent[cur]

    return dp[n], sequence
