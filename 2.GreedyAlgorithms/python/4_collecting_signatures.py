import sys
n = int(input())
segments = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    segments.append((a,b))

for i in range(n):


A = segmaddents.copy()
B = []
for i in range(n):
    xval = max(A[i])
    if xval <= max(A[i+1]):
        A.drop(A[i], A[i+1])
        B.append(xval)
        i = 0
    else:
        continue



        
##greedy strategy

