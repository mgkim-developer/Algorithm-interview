import sys

# n 입력받기
n = int(input())

# 각 집의 색깔 비용 입력 받기
color_cost = []
for i in range(n):
    color_cost.append(list(map(int, sys.stdin.readline().rstrip().split())))
# print(color_cost)

# dp 테이블 생성
dp = color_cost[:]
# print(dp)

for i in range(1, len(dp)):
    # i번째집을 1번째 1번째 색으로 칠하는 최소 비용 = i-1번째 집을 2번째 색으로 칠했을 때와 3번째 색으로 칠했을 때의 최소 비용 + i번째집을 1번째 색으로 칠하는 비용
    # 이것을 i번째집을 1번째 색, 2번째 색, 3번째 색 으로 칠하는 경우를 dp테이블에 누적시키면 마지막 dp테이블의 마지막 인덱스의 비용중에 가장 작은 것을 선택하면 최소비용임.
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i - 1][1])

print(min(dp[-1]))