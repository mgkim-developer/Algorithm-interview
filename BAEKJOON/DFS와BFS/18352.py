from collections import deque
import sys
n, m, k, x = list(map(int, input().split()))
# print(n, m, k, x)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# BFS 메서드 정의
def bfs(graph, x, visited):
    # 큐 구현 (deque 라이브러리)
    queue = deque([x])
    # 현재 노드 방문 처리
    visited[x] =  0
    # 큐가 빌때 까지 반복
    while queue:
        e = queue.popleft()
        # print(e, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[e]:
            if visited[i] == -1:
                visited[i] = visited[e] + 1
                queue.append(i)

visited = [-1] * (n+1)

bfs(graph, x, visited)

for i in range(n+1):
    if visited[i] == k:
        print(i)
if k not in visited:
    print(-1)