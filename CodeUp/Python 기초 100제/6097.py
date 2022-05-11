# h*w는 격자판넓이
# n은 놓을 막대의 갯수
# l막대의 길이, d=0 은 가로 d=1 은 세로, x y 좌표

h, w = input().split()
h = int(h) #격자판의 세로길이
w = int(w)  #격자판의 가로길이
n = int(input())


# h*w 격자판 생성
s = []
for i in range(h):
    s.append([])
    for j in range(w):
        s[i].append(0)

for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    for j in range(l):
        if d == 0:  #가로로 배치할 때
            s[int(x)-1][int(y)+j-1] = 1
        else:   #세로로 배치할 때
            s[int(x)+j-1][int(y)-1] = 1

for i in range(h):
    for j in range(w):
        print(s[i][j],end=" ")
    print()