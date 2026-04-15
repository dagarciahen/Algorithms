import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))



def greedy_strategy(A,B):
    B = B.copy()
    pairs = []
    for a in A:
        best_b = None
        best_value = None

        for b in B:
            value = a*b 
            if best_value is None or value > best_value:
                best_value = value
                best_b = b
        pairs.append((a, best_b))
        B.remove(best_b)
    return pairs

def best_strategy(A,B):
    A = A.copy()
    B = B.copy()
    A.sort()
    B.sort()
    pairs = zip(A,B)
    return pairs



def max_value(pairs):
    suma = 0
    for a,b in pairs:
        suma += a*b
    return suma
pairs1 = greedy_strategy(A,B)
pairs2 = best_strategy(A,B)

print(max_value(pairs1))
print(max_value(pairs2))
