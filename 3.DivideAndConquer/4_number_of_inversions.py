import sys

def Merge(A):
    n = len(A)
    if n <= 1:
        return A, 0
    m = n//2
    B, invB = Merge(A[:m])
    C, invC = Merge(A[m:])
    Af, inv = MergeSort(B,C)
    return Af, invB + invC + inv

def MergeSort(B,C):
    D = []
    i = 0 
    j = 0
    inv = 0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            inv += len(B) - i
            j += 1
    for k in range(i, len(B)):
        D.append(B[k])
    D.extend(C[j:])
    return D, inv

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    result = Merge(A)
    print(result)
