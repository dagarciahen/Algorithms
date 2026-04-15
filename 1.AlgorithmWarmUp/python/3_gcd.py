import sys
a, b = map(int, sys.stdin.readline().split())

def gcd(a,b):
    while b != 0:
        div = a // b
        r = a - div*b 
        # r = a % b
        a = b 
        b = r
    return(a)

print(gcd(a,b))
    


