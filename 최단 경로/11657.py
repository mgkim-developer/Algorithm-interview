import sys

# 노드의 개수 n개, 간선의 개수 m개
n, m = map(int, sys.stdin.readline().rstrip().split())

# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []

# 무한(10억)을 의미하는 INF 변수 선언
INF = int(1e9)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선의 정보 입력
for _ in range(m):
    a, b, c, = map(int, sys.stdin.readline().rstrip().split())
    # a에서 v로 가는 비용이 c
    edges.append((a, b, c))

def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 n번을 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인한다.
        for a, b, c in edges:
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 테이블 갱신
            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:  # n - 1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False


if bellman_ford(1): # 음수 순환이 존재한다면 -1 출력
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1을 출력
        if distance[i] == INF:
            print(-1)
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])