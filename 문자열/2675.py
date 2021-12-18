a = int(input())

for i in range(a):
    b = list(map(str, input().split()))
    for j in range(len(b[1])):
        print((b[1][j])*int(b[0]), end="")
    print()