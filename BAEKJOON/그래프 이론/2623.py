'''
가수 출연 순서를 정하기 위한 조건이 있다.
pd1 : 1->4->3
pd2 : 6->2->5->4
pd3 : 2->3

경우에 따라서 세가지를 모두 만족하는 순서를 정하는 것이 불가능할 수도 있다.
예를 들어 pd3이 2->3대신 3->2로 정해오면,  위의 3가지 조건을 만족하면서 전체 순서를 정하는 것이 불가능하다.

보조 pd들이 만든 순서들이 입력으로 주어질 때, 전체 가수의 순서를 정하는 프로그램을 작성하시오.

- 입력
첫째 줄에는 가수의 수 N(1 <= N <= 1000)과 보조 PD의 수 M(1 <= M <= 100이 주어짐. 가수의 번호는 1~N 이다.
둘쨰 줄부터 각 보조 PD가 정한 순서들이 한 줄에 하나씩 나온다.
각 줄의 맨 앞에는 보조 PD가 담당한 가수의 수가 나온다. 그 뒤로는 그 가수들의 순서가 나온다.

- 출력
출력은 N개의 줄로 이루어지며 한 줄에 하나의 번호를 출력한다.
가수의 출연 순서를 나타낸다. 만약 답이 여럿일 경우에는 아무거나 하나를 출력한다.
만약, 순서를 정하는 것이 불가능할 경우에는 첫째 줄에 0을 출력한다.

i) 우선, 사이클이 존재하지 않으면서 방향성이 있는 그래프를 정렬하는 것이므로,
전형적인 위상정렬 알고리즘 문제로 판단된다.
추가로 출력 조건에서 "답이 여럿일 경우에는 아무거나 하나를 출력하며, 순서정하기가 불가능할 경우 0을 출력한다" 라는 조건또한 위상정렬 알고리즘 문제에서 발생할 수 있는 예외사항에 대한 언급이다.

우선, 위상정렬 알고리즘을 작성해서 적용해보고, 문제에 맞게 조금 변형하든지 하면 될 것 같다.
'''

# 가수의 수 n, 보조 PD의 수 m 입력받기
import sys
from collections import deque

n, m = map(int, input().split())

# 노드간의 관계를 저장할 그래프 선언 및 초기화
graph = [[] for i in range(n + 1)]

# 진입 차수를 저장할 리스트 선언 및 초기화
indegree = [0 for i in range(n + 1)]

# 노드간의 관계를 입력받아서 graph에 저장
for i in range(m):
    tmp_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, tmp_list[0]):
        start = tmp_list[j]
        finish = tmp_list[j + 1]
        graph[start].append(finish)
        indegree[finish] = indegree[finish] + 1

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위해 deque() 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드만 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때 까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 노드와 연결된 노드들의 진입차수 -1하기
        for node in graph[now]:
            indegree[node] = indegree[node] - 1
            if indegree[node] == 0:
                q.append(node)

    if len(result) != n:    # 문제 조건에 따라 위상 정렬 불가시 0 출력
        print(0)
    else:
        for i in result:
            print(i)


topology_sort()