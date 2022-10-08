import heapq
import sys

# 노드의 개수 N, 간선의 갯수E
n, e = map(int, sys.stdin.readline().rstrip().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 모든 간선 정보를 입력 받기
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))
    # 무방향 그래프이므로, b에서 a가는 비용도 c라는 의미
    graph[b].append((a,c))

# 반드시 거쳐야 하는 두개의 노드번호 (1 -> u -> v -> n 또는 1 -> v -> u -> n 경로가 있을 것으로 예상)
u, v =  map(int, sys.stdin.readline().rstrip().split())

# 무한을 의미하는 INF(10억) 변수 선언
INF = int(1e9)

# 시작노드
start = 1

#다익스트라 함수
def dijkstra(start):
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
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
    # 최단 거리 배열을 반환
    return distance


# 출발점이 각각 1, u, v 일때의 최단 거리 배열
original_way = dijkstra(start)
u_way = dijkstra(u)
v_way = dijkstra(v)

u_to_v = original_way[u] + u_way[v] + v_way[n]
v_to_u = original_way[v] + v_way[u] + u_way[n]
result = min(u_to_v, v_to_u)

if result < INF:
    print(result)
else:
    print(-1)

'''
4 5
1 2 3
1 3 1
1 4 1
2 3 3
3 4 4 
2 3

정답 8
'''