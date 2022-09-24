import sys
import heapq

# 노드의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
# print(n, m)

# 시작 노드의 번호
k = int(input())
# print(k)

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n + 1) for _ in range(n+1)] #노드 번호를 인덱스로 사용하기 위해서 n + 1

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # a노드에서 b노드 가는 비용이 c
    graph[a].append((b, c))

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 다익스트라 함수 작성
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])