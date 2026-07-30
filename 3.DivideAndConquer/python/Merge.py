import sys

def MergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    m = n // 2
    B = MergeSort(A[:m])
    C = MergeSort(A[m:])
    D = Merge(B,C)
    return D

def Merge(B,C):
    i = 0
    j = 0
    D = []
    while i < len(B) and j < len(C):
        if B[i] <= C[i]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[i])
            j += 1
    D.extend(B[i:])
    D.extend(C[j:])
    return D

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    result = MergeSort(A)
    print(result)
    



