# 위상 정렬 함수
import sys
from collections import deque


def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for g in graph[now]:
            indegree[g] = indegree[g] - 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[g] == 0:
                    q.append(g)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = ' ')



# 노드의 개수와 간선의 개수 입력
v, e = map(int, sys.stdin.readline().rstrip().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0 for i in range(v + 1)]

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for i in range(v + 1)]

for i in range(e):
    # a 에서 b로 가는 간선
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indegree[b] = indegree[b] + 1   # a에서 b로 가는 간선이면 b의 진입차수가 +1 되기 때문.


topology_sort()


'''
입력 예시
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력 예시
1 2 5 3 6 4 7 
'''