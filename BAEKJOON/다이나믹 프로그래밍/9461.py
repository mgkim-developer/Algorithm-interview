import sys

# 테스트 케이스의 갯수 입력받기
t = int(input())
# print(t)

n_list = [int(sys.stdin.readline().rstrip()) for i in range(t)]
# print(n_list)

dp = [0] * 100

for i in range(max(n_list)):
    if i == 0 or i == 1 or i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]

for i in range(t):
    print(dp[n_list[i]-1])