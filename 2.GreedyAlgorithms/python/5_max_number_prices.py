n = int(input())
F = []
a = 1
suma = 0
for i in range(n):
    r = n - a
    print(f"r {r}")
    b = a +1
    if r > a+i:
        a = a +i
        print(f"a {a}")
        F.append(a)
    else:
        a = a +r 
        print(f"a {a}")
        F.append(a)
        print(F)
            >:::
