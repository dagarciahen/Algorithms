import sys
line = sys.stdin.readline().strip()
n, m = map(int, line)

def get_fibonacci(n, m):
    P = [0, 1]
    while True:
        next_val = (P[:-1] + P[:-2]) % n
        P.append(next_val)
        if P[:-1] == 1 and P[:-2] == 0:
            P = P[:-2]
            break
    period_length = len(P)

    return P[n % period_length]
:

