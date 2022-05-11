import sys
a = 1
b = 1
while a or b != 0:
    a, b = map(int, sys.stdin.readline().split())
    if a or b != 0:
        print(a+b)
    else:
        break
