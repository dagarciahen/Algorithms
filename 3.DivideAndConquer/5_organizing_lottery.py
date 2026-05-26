#python3
import random

import sys 


def QuickSort(S,l,r):
    if l >= r:
        return 
    k = random.randint(l,r)
    S[l], S[k] = S[k], S[l]
    m = Partition(S,l,r)
    QuickSort(S,l,m-1)
    QuickSort(S,m+1,r)

def Partition(S,l,r):
    x = S[l][0]
    j = l
    for i in range(l+1, r+1):
        if S[i][0] <= x:
            j += 1
            S[i], S[j] = S[j], S[i]
    S[l], S[j] = S[j], S[l]
    return j

def sort_points(indexed_points):
    n = len(indexed_points)
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            if indexed_points[j][0] < indexed_points[minindex][0]:
                minindex = j
        indexed_points[i], indexed_points[minindex] = indexed_points[minindex], indexed_points[i]

def compute_coincidences(S,indexed_points):
    K = [0]*len(indexed_points)
    for point, or_index in indexed_points:
        count = 0
        for a,b in S:
            if a > point:
                break
            if a <= point <= b:
                count += 1
        K[or_index] = count
    return K



if __name__ == "__main__":
    s, p = map(int, sys.stdin.readline().split())
    S = [tuple(map(int, sys.stdin.readline().split())) for _ in range(s)]
    P = list(map(int, sys.stdin.readline().split()))
    indexed_points = []
    for i in range(p):
        indexed_points.append((P[i], i))
    sort_points(indexed_points)
    QuickSort(S,0,s-1)
    result = compute_coincidences(S,indexed_points)
    print(*result)
