'''
s 지점에서 출발
목적지 후보들 중 하나가 목적지
최단거리로 갈 것

g와 h 교차로 사이에 잇는 도로를 지나갔음

테스트케이스 개수
n(교차로), m(도로), t(목적지 후보의 개수)
s(예술가들의 출발지), g(g와), h(h의 교차로 사이에 있는 도로를 지나감을 의미)
이후 m개의 줄마다 3개의 정수 a, b, d가 주어진다. a와 b사이에 길이 d의 양방향 도로가 있다는 뜻이다.
그다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. (모두 서로 다른 위치이며, s와 같지 않다.)

i)
g와 h를 무조건 지나야 한다면 두가지 방법이 있다.

출발지점 -> g -> h -> 도착지점
출발지점 -> h -> g -> 도착지점

이 두가지의 최단 거리를 구해주고, 이 최단거리 중 하나라도,
출발지점 -> 도착지점의 최단거리와 같은 경우,
해당 도착 지점을 저장해준다.

'''
import sys
import heapq

# distance 테이블 초기화 하기 위한 INF 선언
INF = int(sys.maxsize)

# 테스트 케이스 개수 T
T = int(sys.stdin.readline().rstrip())

# 다익스트라 함수 작성
def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])    # heap에 heqpq.heappush로 [0, start] 넣어줌
    distance = [INF] * (n + 1)  # distance 테이블 초기화
    distance[start] = 0 # distance 테이블의 start 인덱스에 해당하는 가중치(거리) 값을 0으로 초기화

    while heap: # heap에 데이터가 존재하지 않을 때 까지 반복
        weight, now = heapq.heappop(heap)
        for node_x, node_x_w in graph[now]:
            cost = node_x_w + weight
            if cost < distance[node_x]:
                distance[node_x] = cost
                heapq.heappush(heap, [cost, node_x])
    return distance

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split())
    s, g, h = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    x = []
    for _ in range(t):
        x.append(int(sys.stdin.readline().rstrip()))

    s_cost = dijkstra(s)
    g_cost = dijkstra(g)
    h_cost = dijkstra(h)
    answer = []

    for i in x:
        # 출발지점 -> g -> h -> 도착지점 이 경로의 가중치가 출발지점 -> 도착목표 i까지의 가중치와 같거나 or 출발지점 -> h -> g -> 도착지점 이 경로의 가중치가 출발지점 -> 도착목표 i까지의 가중치와 같으면
        if s_cost[g] + g_cost[h] + h_cost[i] == s_cost[i] or s_cost[h] + h_cost[g] + g_cost[i] == s_cost[i]:
            answer.append(i)    # 정답 리스트에 저장

    answer.sort()
    for i in range(len(answer)):
        print(answer[i], end=' ')
    print()
