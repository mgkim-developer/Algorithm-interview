# 10 * 10 크기의 2차원 배열로 입력받음

s = []
for i in range(10):
    w = list(map(int, input().split()))
    s.append(w)

x = 1
y = 1
while True:
    if s[x][y] == 0:
        s[x][y] = 9
    elif s[x][y] == 2:
        s[x][y] = 9
        break

    if (s[x][y+1]==1 and s[x+1][y]==1) or (x==9 and y==9):
        break

    if s[x][y+1] != 1:
        y += 1
    elif s[x+1][y] != 1:
        x += 1

for i in range(0, 10):
    for j in range(0, 10):
        print(s[i][j], end=' ')
    print()