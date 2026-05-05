import sys
import random

def quick_sort(A,l,r):
    if l >= r:
        return
    k = random.randint(1, r)
    A[k], A[l] = A[l], A[k]
    (m1, m2) = Partition(A,l,n-1)
    quick_sort(A, l, m1-1)
    quick_sort(A, m2+1,r)

def Partition(A, l, r):
    x = A[l]
    i = l +1
    lt = l
    gt = r
    
    while i <= gt:
        if A[i] < x:
            A[lt], A[i] = A[i], A[lt]
            lt +=1
            i +=1
        elif A[i] > x:
            A[gt], A[i] = A[i], A[gt]
            gt -=1
        else:
            i +=1
    return (lt, gt)

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    l = 0
    r = len(A)-1
    result = quick_sort(A,l,r)
    print(A)
