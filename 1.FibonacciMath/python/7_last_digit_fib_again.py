import sys
line = sys.stdin.readline().strip()
m, n= map(int, line)

def last_fucking_fib(m, n):
    P = [0, 1]
    while True:
        next_val = (P[-2] + P[-1]) % 10 
        P.append(next_val)
        if P[-2] == 0 and P[-1] == 1:
            P = P[:-2]
            break
    period = len(P)
    index1 = (n+2) % period
    index2 = (m+1) % period
    F_n_plus2 = P[index1]
    F_m_plus1 = P[index2]
    result = F_n_plus2 - F_m_plus1
    return result

print(last_fucking_fib(m,n))
