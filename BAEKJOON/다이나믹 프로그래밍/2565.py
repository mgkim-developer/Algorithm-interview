'''
입력으로 첫번쨰 줄에 n이 주어지고,
두번째 줄부터 n + 1 번째 줄 까지
각각 A to B가 주어진다. (전깃줄의 연결 정보)

모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구해야 한다.

전깃줄이 서로 교차하지 않기 위해서는,
1번에서 출발한 전깃줄의 도착지점은  그 이후의 번호에서 출발한 전깃줄의 도착지점들보다 낮은 번호에 도착해야 한다.
1번에서 출발한 전깃줄의 도착지점을 a1이라고 하면,
2번에서 출발한 전깃줄의 도착지점은 a1 < a2 여야 하며,
3번에서 출발한 전깃줄의 도착지점은 a1 < a2 < a3 여야 서로 교차하지 않을 것이다.

그렇다면, 우리는 최장 증가 부분 수열(LIS)를 구하고,
전체 n개에서 최장 증가 부분 수열의 길이를 빼준 값의 갯수만큼 전깃줄을 제거하면 서로 교차하지 않는 전깃줄을 만드는 최적해라고 이야기 할 수 있을 것이다.

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