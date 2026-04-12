P = [i for i in range(12)]
# [0,1,2,3,...11]

hour = int(input())
index = hour % len(P) #len(P) = 12
# si pasan 12 horas 12 % 12 = 0
#si pasan 13 horas 13 % 12 = 1 (empieza ciclo otra vez)
# si pasn 14 horas 14 % 12 = 2 
result = P[index] 
print(result)
