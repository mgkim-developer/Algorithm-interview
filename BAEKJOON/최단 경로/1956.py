import sys

# v개의 노드 e개의 간선
v, e = list(map(int, input().split()))

# 무한(10억)을 의미하는 INF 변수 선언
INF = int(1e9)

# 2차원 리스트르르 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 -------- 문제를 잘 살펴보면, 다시 시작점으로 돌아오는 사이클을 찾는 것을 원하기 때문에 자기 자신에게 돌아오는 비용을 0으로 처리하면 안됌.
# for a in range(1, v + 1):
#     for b in range(1, v + 1):
#         if a == b:
#             graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for  _ in range(e):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c
print(graph)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(v + 1):
    for a in range(v + 1):
        for b in range(v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
result = INF

for i in range(1, v + 1):
    result = min(result, graph[i][i])

if result == INF:
    print(-1)
else:
    print(result)