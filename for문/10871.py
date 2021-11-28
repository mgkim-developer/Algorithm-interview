import sys

N, X = map(int, input().split())
a = []
c = []
b = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    a.append(b[i])
    if a[i] < X:
        c.append(a[i])
for k in range(c):
    print(c[k])
