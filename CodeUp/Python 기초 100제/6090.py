a, m, d, n = map(int, input().split())

k = a

for i in range(1, n):
    k = k * m + d

print(k)





