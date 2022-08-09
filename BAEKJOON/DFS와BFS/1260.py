from collections import deque
import sys
n, m, v = map(int,input().split())
graphs = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graphs[a].append(b)
    graphs[b].append(a)
for i in range(len(graphs)):
    graphs[i].sort()
# print(graphs)

# DFS 메서드 정의
def dfs(graph, s, visited):
    # 현재 노드를 방문 처리
    visited[s] = True
    print(s, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[s]:
        if visited[i] == False:
            # print(visited)
            dfs(graph, i, visited)
#
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (n+1)

# 정의된 DFS 함수 호출
dfs(graphs, v, visited)


#-----------------------------------------------------

# BFS 메서드 정의
def bfs(graph, s, visited):
    # 큐 구현 (deque 라이브러리)
    queue = deque([s])
    # 현재 노드 방문 처리
    visited[s] =  True
    # 큐가 빌때 까지 반복
    while queue:
        e = queue.popleft()
        print(e, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[e]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)

print()
bfs(graphs, v, visited)