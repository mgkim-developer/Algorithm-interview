import sys

n = int(input())

num_list = []

for i in range(n):
    num_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
# print(num_list)

dp = [[0] * i for i in range(1, n + 1)]
# print(dp)
dp[0][0] = num_list[0][0]
# print(dp)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 왼쪽 끝 값인 경우
            dp[i][0] = dp[i-1][j] + num_list[i][j]
        elif j == i:    # 오른쪽 끝 값인 경우
            dp[i][j] = dp[i-1][j-1] + num_list[i][j]
        else:   # 가장 자리가 아닌 경우 자신을 기준으로 왼쪽 위 값과 오른쪽 위 값 중 더 큰 값을 자기자신과 더해주기
            dp[i][j] = max(dp[i-1][j-1] + num_list[i][j], dp[i-1][j] + num_list[i][j])

print(max(dp[-1]))