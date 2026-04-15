n = int(input())
F = [0, 1]
for i in range(2, n+1):
    next_last_digit = (F[i-2] + F[i-1] ) % 10
    F.append(next_last_digit)

print(next_last_digit)

