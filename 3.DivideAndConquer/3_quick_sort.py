import sys
import random
n = sys.stdin.readline()

def quick_sort(A, l,r):
    if l >=r:
        return
    k = random.randint(l,r)
    A[l], A[k] = A[k], A[l]
    (m1, m2) = Partition(A,l,r)
    quick_sort(A,l, m1-1)
    quick_sort(A,m2+1,r)


def Partition(A,l,r):
    x = A[l]
    m1 = l
    m2 = r
    i = l +1
    while i <= m2:
        if A[i] < x:
            A[i], A[m1] = A[m1], A[i]
            m1++
            i++
        else if A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2--
        else: 
            i++
   return (m1, m2)

    
if __name__ = '__main__':
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    quick_sort(A, 0, len(A)-1)
