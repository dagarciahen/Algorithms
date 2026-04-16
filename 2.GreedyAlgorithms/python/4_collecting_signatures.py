import sys
n = int(input())
segments = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    segments.append((a,b))

##greedy strategy

