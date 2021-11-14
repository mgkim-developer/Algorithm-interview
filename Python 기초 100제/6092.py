n = int(input())
a = list(map(int, input().split()))

d = []
for i in range(23):
    d.append(0)

for i in range(n):
    d[a[i]-1] += 1

for i in range(0, 23):
    print(d[i], end=" ")

