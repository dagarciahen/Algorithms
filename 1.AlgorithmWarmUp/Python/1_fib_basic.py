import sys 
n = int(input())
F = [0, 1]
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))

    
