'''
N명의 학생들을 키 순서대로 줄을 세우려고 함.
두 학생의 키를 비교한 데이터가 있을 때,
이 데이터를 이용하여 줄을 세워야 한다.

-입력
첫째 줄에 N(1 <= N <= 32,000), M(1 <= M <= 100,000)이 주어진다. 이때 M은 키를 비교한 횟수이다.
다음 M개의 줄에 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미.

학생들의 번호는 1번부터 N번임.

-출력
첫째 줄에 학생들을 앞에서부터 줄을 세운 결과 출력.
답이 여러가지인 경우에는 아무거나 출력 할 것.

i)
위상 정렬을 이용하여 풀이하면 될 것으로 예상된다.
+ 위상정렬의 경우 한 단계에서 큐에 여러개의 원소가 들어가면 답안이 여러개일 수 있음.
'''

# n은 학생들의 끝번호, m은 키를 비교한 횟수.
import sys
from collections import deque

n, m = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0 for i in range(n + 1)]

# 각 노드에 연결된 정보를 담기 위한 그래프
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # a 학생이 b학생 앞에 서야한다는 의미
    graph[a].append(b)
    indegree[b] = indegree[b] + 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for j in graph[now]:
            indegree[j] = indegree[j] - 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                q.append(j)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = ' ')

topology_sort()