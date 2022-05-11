n = int(input())
k = list(map(int, input().split()))
# k.sort()
# print(k[0])

min = k[0]
for i in range(0, n):
    if k[i] < min:
        min = k[i]

print(min)
