from collections import deque

# 테스트 케이스 만큼 반복
for testcase in range(int(input())):
    # 노드의 갯수 입력 받기
    n = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n + 1) for i in range(n + 1)]
    #작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True  # i노드가 가리키는 노드인덱스(j)를 True로 초기화
            indegree[data[j]] = indegree[data[j]] + 1 # i노드가 가리키는 노드의 친입차수를 +1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split()) # a가 b보다 순위가 낮았는데 올해 a가 더 높아진 경우
        # 간선의 방향 뒤집기
        if graph[a][b]: # a가 b를 가리키고 있던 경우 (a가 b보다 컷던 경우)
            graph[a][b] = False # a가 b를 가리키는 간선을 끊기
            graph[b][a] = True # b가 a를 가리키는 간선을 연결하기
            indegree[a] = indegree[a] + 1
            indegree[b] = indegree[b] - 1
        else:   # a가 b를 가리키고 있지 않던 경우  (a가 b보다 작았던 경우)
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] = indegree[a] - 1
            indegree[b] = indegree[b] + 1

    # 위상 정렬(Topology Sort) 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내 사이클이 존재하는지 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면(진입차수가 0인 것이 없다면) 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미(동시에 진입차수가 0이 된 노드가 2개 이상인 경우)
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] = indegree[j] - 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우(데이터에 일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif certain == False:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()



'''
[a][b]가 True라는 것은
a가 b를 가리키고있는다는 
a가 b를 가리키고 있는다는 뜻은
a가 b보다 크다는 뜻
'''