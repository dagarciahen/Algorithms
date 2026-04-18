import sys
n = int(input())
segments = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    segments.append((a,b))

#sort by by from low to max
points = []
for i in range(n):
    for j in range(0, n-i-1):
        if segments[j][1] > segments[j+1][1]:
            segments[j], segments[j+1] = segments[j+1], segments[j]

curr_point = -1
for a,b in segments:
    #x must be b>x>
    if a > curr_point:
        curr_point = b
        points.append(curr_point)

print(len(points))
print(*points)
#print(" ".join(map(str,points)))




