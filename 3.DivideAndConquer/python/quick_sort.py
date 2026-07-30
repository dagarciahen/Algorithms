import sys 
import random

def quick_sort(A,l,r):
    if l >= r:
        return
    k = random.randint(l,r)
    A[l], A[k] = A[k], A[l]
    (m1, m2) = Partition(A,l,r)
    quick_sort(A,l,m1-1)
    quick_sort(A,m2+1, r)

def Partition(A,l,r):
    x = A[l]
    lt = l
    i = l + 1
    gt = r
    while i <= gt:
        if A[i] < x:
            A[i], A[lt]  = A[lt], A[i]
            lt +=1
            i += 1
        elif A[i] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -=1
        else:
            i += 1
    return (lt, gt)

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    l = 0
    r = len(A)-1
    quick_sort(A,l,r)
    print(A)

