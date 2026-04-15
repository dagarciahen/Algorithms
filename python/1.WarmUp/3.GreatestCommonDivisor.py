import sys
line = sys.stdin.readline().strip()
a, b = map(int, line.split())

# a/b -> a = b*q + r 
def gcd(a, b):
    while b > 0:
        q = a//b
        r = a - b*q
        a = b
        b = r
    return(a)

