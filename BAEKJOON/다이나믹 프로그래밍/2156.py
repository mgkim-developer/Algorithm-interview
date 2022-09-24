import sys

n = int(input())
# print(n)

graph_ml = []
for i in range(n):
    graph_ml.append(int(sys.stdin.readline().rstrip()))
graph_ml = [0] + graph_ml # dp와 인덱스를 동일하게 해주기 위해여 [0]을 맨앞에 추가
# print(graph_ml)

dp = [0] * (n + 1)

# 1과 2의 위치까지는 최대값이 연속으로 마신 경우이므로 초기값을 지정
dp[1] = graph_ml[1]
if n >= 2:
    dp[2] = dp[1] + graph_ml[2]
# print(dp)


for i in range(3, n + 1):
    # 현재 위치의 와인을 마시고 바로 전 와인을 마셨다는 것은 -3 위치의 최대값에서 하나 건너 뛴 경우다.
    # 현재 위치의 와인을 마시고 이전 와인이 건너 뛴 와인이라면 -2 위치의 최대값을 더한 경우다.
    # 현재 위치의 와인을 마시지 않았다면 -1위치의 최대값이 현재 위치의 최대값이다.
    dp[i] = max(dp[i - 3] + graph_ml[i - 1] + graph_ml[i], dp[i - 2] + graph_ml[i], dp[i - 1])

# print(dp)
print(dp[n])