import sys

first_string =  list(sys.stdin.readline().strip())
second_string = list(sys.stdin.readline().strip())

def edit_distance(string1, string2):
    n = len(string1)
    m = len(String2)
    dp = []

    for i in range(n+1):
        row = []
        for j in range(m+1):
            row.append(0)
        dp.append(row)
    # dp = [[0]*(m+1) for _ in range(n+1)]

    #first row and first columns

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    val1 = val2= val3 = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            #insertion
            if j > 0:
                val1 = dp[i][j-1] +1

            #deletion
            if i > 0:
                val2 = dp[i-1][j] +1

            if string1[i] == string2[j]:
                val3 = dp[i-1][j-1]

            else:
                val3 = dp[i-1][j-1] +1

            dp[i][j] = min(val1, val2, val3)

    return dp[n][m]




V
