m = int(input())
c_10 = 0
c_5 = 0
c_1 = 0
q = m
while (q) >= 10:
    q = q - 10    
    c_10 += 1

while (q) >= 5:
    q = q - 5 
    c_5 += 1
while ( q) > 0:
    q = q -1 
    c_1 += 1

result = c_10 + c_5 + c_1 
print(result)

