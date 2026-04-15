n = int(input())

def last_digit(n):
    if n <= 1:
        return n
    P = [0, 1]
    
    while True:
        next_val = (P[-2] + P[-1]) % 10 
        P.append(next_val)
        if (P[-2] == 0 and P[-1] == 1):
            P = P[:-2]
            break
    periodo = len(P)
    index = (n+2)% periodo
    F_n_plus2 = P[index]
    result = (F_plus2 -1 ) % 10


    return result

print(last_digit(n))

