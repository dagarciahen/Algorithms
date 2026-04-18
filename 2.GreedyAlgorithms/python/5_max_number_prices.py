n = int(input())
suma = 0
F = []
k = 0
while suma < n:
    k +=1
    print("k")
    print(k)
    suma += k
    print("suma")
    print(suma)
    k_plus1 = k +1
    sumk = suma + k_plus1
    print("sumk")
    print(sumk)
    if sumk > n:
        r = n - suma
        print("r")
        print(r)
        k += r 
        print("k")
        print(k)
        suma += k
        F.append(k)
    else:
        print("k else")
        print(k)
        F.append(k)
print(F)
