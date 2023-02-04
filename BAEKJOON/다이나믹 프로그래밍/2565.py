'''
두 전보대 A와 B사이에 하나 씩 전깃줄 추가
그러다보니 전깃줄이 서로 교차하는 경우가 발생
합선의 위험이 있어 이들 중 몇개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 함.

'''

import sys

n = int(sys.stdin.readline().rstrip())
wire = [[] for _ in range(n)]
for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    wire[i] = [start, end]

dp = [0 for i in range(n)]

# 각 요소의 인덱스 0번 데이터 기준으로 정렬
sort_wire = sorted(wire, key=lambda  wire: wire[0]) # 각 요소의 0번째 인덱스요소 기준으로 오름차순 정렬

for i in range(n):
    for j in range(i):
        if sort_wire[i][1] > sort_wire[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] = dp[i] + 1

print(n - max(dp))  # n에서 LIS길이를 빼주면 제거해야하는 전깃줄 갯수