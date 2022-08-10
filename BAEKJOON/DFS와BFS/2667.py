# n 입력 받기
n = int(input())

# 2차원 리스트의 맵 정보 입력받기
graph = []
count_list = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    count = 0
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        count = count + 1
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # print(graph)
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        count_list.append(count)
        return True
    # return False

count_result_list = []

# 모든 노드(위치)에 대하여 집 채우기
result = 0
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            # print(count_list)
            count_result = 0
            for k in range(len(count_list)):
                count_result = count_result+1
                count_list.pop()
            count_result_list.append(count_result)

count_result_list.sort()
print(result)
for i in range(len(count_result_list)):
    print(count_result_list[i])