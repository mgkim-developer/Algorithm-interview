import sys

N, X = map(int, input().split())
a = []

b = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    a.append(b[i])
    if a[i] < X:
        print(a[i], end=" ")

