import sys
line = sys.stdin.readline().strip()
n, m = map(int, line)

def period_calculation(m):
    F = [0, 1]
    P = [0, 1]
    i = 2
    while True:
        F.append(F[i-1] + F[i-2])
        P.append(F[i] % m)
        (curr, prev ) = (P[-1], P[-2])
        if curr == 1 and prev == 0:
            P = P[:-2]
            break
        else:
            i += 1
    return (len(P), F)


def Fibonacci(n, m):
    (period, F) = period_calculation(m)
    n = n % period
    result = F[n] % m
    return result

print(Fibonacci(n, m)
