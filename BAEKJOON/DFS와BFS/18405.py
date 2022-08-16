import sys
from collections import deque


# n은 크기 k는 바이러스 종류
n, k = map(int, input().split())
# print(n, k)

# 공간 정보 저장할 리스트
zone = []

# 바이러스 저장할 리스트
virus = []

# 입력 공간 받아서 zone에 저장
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    zone.append(line)
    for j in range(n):
        if zone[i][j] != 0:
            virus.append((zone[i][j], i, j))

# 숫자가 작은 바이러스부터 증식 되도록 정렬
virus.sort()

# s는 초, x1는 행, y1는 열
s, x1, y1 = map(int, input().split())
# print(s, x1, y1)

# 상하좌우
dx = [-1, 1, 0, 0]  # 이게 행이므로 세로
dy = [0, 0, -1, 1]  # 이게 열이므로 가로

# BFS정의
def bfs(graph, virus, x1, y1):
    # 큐생성
    queue = deque(virus)
    count = 0
    while queue:
        if count == s:
            break
        for k in range(len(queue)):
            type, x, y = queue.popleft()
            # 해당 바이러스의 상하좌우중에 빈곳이 있으면 바이러스 증식
            for i in range(4):  # 좌우하상 탐색
                ndx = x + dx[i]
                ndy = y + dy[i]
                # graph 내부이면
                if 0 <= ndx < n and 0 <= ndy < n:
                    if graph[ndx][ndy] == 0:
                        graph[ndx][ndy] = graph[x][y]
                        queue.append(([ndx, ndy], ndx, ndy))
        count = count + 1
    return print(graph[x1-1][y1-1])

bfs(zone, virus, x1, y1)