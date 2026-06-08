import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
n = len(string1)
m = len(string1)

dp = []
for i in range(n+1):
    row = []
    for j in range(m+1):
        row.append(0)
    dp.append(row)

def OutputAlignment(i,j):

    if i == 0 and j == 0:
        return
    #insertion
    if i > 0 and dp[i][j] == dp[i][j-1] +1:
        OutputAlignment(i,j-1)
         print("-", string2[j-1])
    #deletion
    elif j > 0: 
        if dp[i][j] == dp[i-1][j] +1:
            OutputAlignment(i-1, j)
            print(string1[i-1], "-")

    else:
        OutputAlignment(i-1,j-1)
        print(string1[i-1], string2[j-1])





