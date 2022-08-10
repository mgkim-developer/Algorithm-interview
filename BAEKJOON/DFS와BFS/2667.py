# n 입력 받기
n = int(input())

# 2차원 리스트의 맵 정보 입력받기
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        global count    # 이게 출력 핵심 이었음. 리팩토링 완료.
        count = count + 1
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # print(graph)
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

count = 0
count_result = []
# 모든 노드(위치)에 대하여 집 채우기
result = 0

for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            count_result.append(count)
            result = result + 1
            count = 0

print(result)
count_result.sort()
for i in count_result:
    print(i)