import sys
from collections import deque
import copy

# n 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph_input = []
for i in range(n):
    graph_input.append(list(map(int, sys.stdin.readline().split())))
# print(graph)

# 안전 영역 크기 최댓값 결과
result = 0

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 감염 BFS 메서드 정의
def bfs(graph):
    global result
    graph = copy.deepcopy(graph_input)
    # 큐 구현 (deque 라이브러리)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2: # 바이러스가 있는 공간이면
                queue.append([i, j]) # 큐에 삽입

    # 큐가 빌때 까지 반복
    while queue:
        # print(queue)
        x, y = queue.popleft()
        # print("x", x, "y", y)
        # 해당 공간과 연결된, 아직 바이러스가 없는 공간을 큐에 삽입
        for i in range(4):  # 좌우하상 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 공간범위 이내인 경우
                if graph[nx][ny] == 0:  # 해당 좌표가 빈 공간이면
                    graph[nx][ny] = 2   # 해당공간에 바이러스 전염시키기
                    queue.append([nx, ny])  # 큐에 해당 공간 삽입
        # print(queue)

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                count = count + 1
    result = max(result, count)


    # for i in range(len(graph)):
    #     # print(graph[i])

def fense(x):   # 펜스 0개부터 3개가 될 때까지 펜스를 치다가 펜스가 3개가 되면 bfs 호출
    if x == 3:
        bfs(graph_input)
        return
    for i in range(n):
        for j in range(m):
            if graph_input[i][j]==0:
                graph_input[i][j] = 1
                fense(x+1)
                graph_input[i][j] = 0


fense(0)
print(result)