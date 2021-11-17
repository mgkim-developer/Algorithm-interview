d = []
for i in range(19):
    s = list(map(int, input().split()))
    d.append(s)
n = int(input())
for i in range(n):
    x, y = input().split()

    #   잘못 생각한 방법은, 좌표가(x,y)라면, d[y][x]라고 생각하고 문제를 풀었으나,
    #   테스트케이스에서 발견된 오류를 바탕으로 다시 생각해 보니, 애초에 문제의 그림에서 (3,2)는 a[j][3]으로 표현되어 있었고, 문제에서 설명한(x,y)는
    #   우리가 일반적으로 생각하는 (x좌표의값, y좌표의값) 이 아니라, 그냥 변수x 변수y였고, x는 Y절편값, y는 X절편값이었으므로 d[y][x]라고 작성하면 틀린다.
    #   따라서 d[x][y]라고 써야 좌표(x, y)가 된다.
    #   변수명으로 x가 x좌표값, y는 y좌표로 착각하지 않도록 주의하자.
    # --------------------------------------
    # for j in range(0, 19) :
    #   if d[int(y)-1][j]==0 :
    #      d[int(y)-1][j]=1
    #   else :
    #      d[int(y)-1][j]=0
    #
    #   if d[j][int(x)-1]==0 :
    #      d[j][int(x)-1]=1
    #   else :
    #      d[j][int(x)-1]=0
    # --------------------------------------

    for j in range(0, 19):
        if d[j][int(y) - 1] == 0:
            d[j][int(y) - 1] = 1
        else:
            d[j][int(y) - 1] = 0

        if d[int(x) - 1][j] == 0:
            d[int(x) - 1][j] = 1
        else:
            d[int(x) - 1][j] = 0

for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print()

# 모든 y의 해당 x값을 바꿔야함 반대로


