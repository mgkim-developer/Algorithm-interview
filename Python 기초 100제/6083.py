r, g, b = map(int, input().split())
# r, g, b에 각각 양의 정수가 입력되고, 그 수들의 조합을 출력해야한다.
# 예를들어 2 2 2 가 입력되면
# 0 0 0
# 0 0 1
# 0 1 0
# 이런식으로
n = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            n= n+1
print(n)