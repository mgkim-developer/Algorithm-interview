import sys

# 노드의 개수 n
n = int(input())

# 간선의 개수 m
m = int(input())

# 무한(10억)을 의미하는 INF 변수 생성
INF = int(1e9)

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화 한다.
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = min(c, graph[a][b]) # 시작도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다 라는 조건이 있는 것을 감안해서 최소비용 간선 적용

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('0', end = " ")
        else:
            print(graph[i][j], end = " ")
    print()