def Fibonacci_LastDigit(n):
    F = []
    F[0] = 0
    F[1] = 1
    if n <= 1:
        return F[n]
    else:
        F[i] % 10 = (F[i-1] + F[i-2]) % 10
        return F[i]
    
