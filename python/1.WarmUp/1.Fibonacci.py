def Fibonacci(n):
    #Works well until n =20
    if n <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

