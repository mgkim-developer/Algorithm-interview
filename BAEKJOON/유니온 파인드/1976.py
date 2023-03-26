'''
N개의 도시가 있다.
임의의 두 도시 사이에 길이 있을 수도 있고, 없을 수도 있다.

여행일정이 주어졌을 때, 이 여행 경로가 가능한 것이지 알아보자.
중간에 다른 도시를 경우해도 OK
ex) 도시가 5개 있고,
A-B
B-C
A-D
B-D
E-A 의길이 잇고,
여행계획이 ECBCD 라면 E-A-B-C-B-C-B-D 라는 여행경로를 통해 목적 달성 OK

도시들의 개수와 도시간의 연결 여부가 주어져있고, 여행계획이 순서대로 주어져있을 때,
여행이 가능한지 판별하는 프로그램 작성 할 것.(같은 도시를 여러 번 방문 OK)

- 입력
첫 줄에 도시의 수 N (N <= 200)
여행에 속한 도시들의 수 M (M <= 1000)
다음 N개의 줄에는 N개의 정수가 주어진다.
i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다. 1이면 연결된 것이고 0이면 연결되지 않은 것. (만약 A와 B가 연결되었으면 B와 A도 연결되있는 것)
마지막 줄에는 여행 계획이 주어진다.

i)
일단, 입력받으 도시연결정보를 토대로 find_parent 함수와 union_parent 함수를 이용하여 연결하고,
여행 계획에 속한 도시들의 부모가 같은지 확인하면 될 것이다.
부모가 같다면, 경유지를 거쳐서라도 도시들이 연결되어 있는 것이기 때문이다.

'''
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y, rank):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)

    # 두 값의 root가 같으면(이미 같은 트리) 합치지 않음
    if rootX == rootY:
        return

    # rank가 큰 트리에 rank가 작은 트리에 붙인다
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else: # 만약 rank가 같다면 임의로 rootX 트리에 rootY 트리를 붙인다
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1


# 도시의 수
n = int(input())
# 여행에 속한 도시들의 수
m = int(input())

# 도시들의 연결정보를 저장할 list
chart = []
for i in range(n):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    chart.append(info)

# 여행 계획 입력받기
plan = list(map(int, input().split()))
# 입력받은 도시들의 연결정보를 토대로
chart_map = []
for i in range(n):
    for j in range(n):
        if chart[i][j] == 1:
            chart_map.append([i+1, j+1])

# parent 리스트 선언 및 초기화
parent = [i for i in range(n + 1)]

# rank 리스트 선언 및 초기화
rank = [0 for i in range(n + 1)]


for i in range(len(chart_map)):
    a, b = chart_map[i]
    union_parent(parent, a, b, rank)

# 각 여행 목적지의 root를 찾아서 저장하고, 추후 set으로 변형시켜서 len이 1인지 확인하기 위함.
# 만약 len이 1이면 YES 1이 아니면 NO 출력할 것임
validation = []
for i in range(len(plan)):
    goal = find_parent(parent, plan[i])
    validation.append(goal)
set_validation = list(set(validation))

if len(set_validation) == 1:
    print('YES')
else:
    print('NO')
