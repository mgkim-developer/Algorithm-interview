from collections import deque

n, l, r = map(int, input().split())
# print(n, l, r)

world_map = []

for i in range(n):
    world_map.append(list(map(int, input().split())))
# print(world_map)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):
    # (x, y)의 위치와 연결된 나라 정보를 담는 연합 리스트
    linkend_country = []
    linkend_country.append((x, y))
    # 큐 생성
    queue = deque()
    queue.append((x, y))
    yeonhab[x][y] = index   # 현재 좌표에 현재 연합의 번호 할당
    all_people = world_map[x][y]    # 현재 연합의 전체 인구 수
    yeonhab_country_number = 1 # 현재 연합에 속한 국가 수
    while queue:
        x, y = queue.popleft()
        # 상하좌우 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접해있는 나라를 확인
            if 0 <= nx < n and 0 <= ny < n and yeonhab[nx][ny] == -1: # n * n  범위 안 이면서, 연합에 편입되지 않은 상태이면,
                # 인접해 있는 나라와 인구차이가 l명 이상, r명 이하라면,
                if l <= abs(world_map[nx][ny] - world_map[x][y]) <= r:
                    queue.append((nx, ny))
                    # 연합에 추가
                    yeonhab[nx][ny] = index
                    all_people = all_people + world_map[nx][ny]
                    yeonhab_country_number = yeonhab_country_number + 1
                    linkend_country.append((nx, ny))
    # 연합에 속한 국가들끼리 인구 분배
    for i, j in linkend_country:
        world_map[i][j] = all_people // yeonhab_country_number
    return yeonhab_country_number

day = 0

# bfs를 정상적으로 구현했을 때 이후 액션
while True:
    yeonhab = [[-1] * n for k in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if yeonhab[i][j] == -1:
                bfs(i, j, index)
                index = index + 1
    if index == n * n:
        break
    day = day + 1

print(day)