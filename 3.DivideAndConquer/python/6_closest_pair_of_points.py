import sys
import random
import math

def distance(P1, P2):
    (x1, y1) = P1
    (x2, y2) = P2

    distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return distance

def distance_three_points(P1, P2, P3):
    d1 = distance(P1,P2)
    d2 = distance(P1,P3)
    d3 = distance(P2,P3)
    distance = min(d1, d2, d3)
    return distance

def QuickSort(A, l, r, key):
    if l >= r:
        return
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    m = Partition(A,l, r, key)
    QuickSort(A,l, m-1, key)
    QuickSort(A,m+1,r,key)

def Partition(A,l, r, key):
    x = A[l]
    x_value = A[l][key]
    j = l
    for i in range(l+1, r+1):
        if A[i][key] <= x_value:
            j = j +1
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def closestPair(X,Y):
    n = len(X)
    if n == 2:
        return distance(X[0], X[1])
    if n == 3:
        return distance_three_points(X[0], X[1], X[2])
    mid = n // 2
    midPoint = X[mid]
    dl = closestPair(X[:mid], Y)
    dr = closestPair(X[mid:], Y)
    d = min(dl, dr)

    S = []
    for p in Y:
        if abs(p[0]-midPoint[0]) < d:
            S.append(p)
    for i in range(len(S)):
        for j in range(1, 8):
            if i +j < len(S):
                d = min(d, distance(S[i], S[i+j]))
    return d

if __name__ == "__main__":
    n = int(input())
    P = []
    for _ in range(n):
        (a,b) = map(int, sys.stdin.readline().split())
        P.append((a,b))
    X = P.copy()
    Y = P.copy()
    QuickSort(X, 0, len(X)-1, key=0)
    QuickSort(Y, 0, len(Y)-1, key=1)
    result = closestPair(X,Y)
    print(result)




