def Fibonacci(n):
    F = []
    if n <= 1:
        return n
    else:
        F[n] = F[n-1] + F[n-2]
        return F[n]
    

