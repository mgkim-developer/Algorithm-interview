'''
사이클 게임은 두 플레이어가 차례대로 돌아가며 진행하는 게임.
선 플레이어가 홀수 번째 차례 진행
후 플레이어가 짝수 번째 차례 진행
게임 시작 시 0부터 n - 1 까지 고유한 번호가 부여된 평면상의 점 n개가 주어지며, 이중 어느 세 점도 일직선 위에 놓이지 않음.(그래프 형태라는 뜻으로 해석함)
매 차례마다 플레이어는 두 노드를 선택해 간선을 연결함. 이전에 있던 간선을 다시 그을수는 없지만, 이미 있는 간선과 교차하는 것은 가능하다.
게임을 진행하다가 처음으로 사이클을 완성하면 게임종료.

노드의 갯수 n과 m번쨰 차례 까지의 게임진행 상황이 주어지면,
사이클이 완성 되었는지를 판단하고, 사이클이 완성되었다면,
몇 번째 차례에서 사이클이 완성되었는지, 혹은 아직 게임이 진행중인지를 판단하는 프로그램을 작성해야함.

- 입력
첫 번째 줄에는 점의 개수를 나타내는 정수 n (3 <= n <= 500,000) 노드의 번호는 0번부터 n - 1번까지임, 진행된 차례의 수를 나타내는 정수 3 <= m <= 1,000,000 주어짐.
이어지는 m개의 입력 줄에는 각각 i번째 차례에 해당 플레이어가 선택한 두 점의 번호가 주어짐 (1 <= i <= m)

- 출력
m번째 차례까지 게임을 진행한 상황에서 사이클이 이미 완성되어 게임이 종료되었다면, 사이클이 처음 만들어진 차례의 번호를 양의 정수로 출력하고,
만약, m 번의 차례를 모두 처리한 이후에도 종료되지 않았다면 0을 출력할 것.

i)
유니온 파인드를 이용해서 사이클 유무를 판단하는 것이 핵심으로 보여진다.
'''

# 부모노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 유니온 연산을 수행하는 함수
def union_parent(parent, x, y, rank):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)

    # 만약 두 루트의 값이 같으면 이미 같은 트리이므로 합치지 않음
    if rootX == rootY:
        return

    # union-rank 최적화 적용
    # rank가 더 큰 트리에 작은 트리를 붙인다.
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:   # 만약 rank가 같다면 임의로 rootX트리에 rootY트리를 붙인다.
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1


import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

info = [[] for i in range(m + 1)]

for i in range(1, m + 1):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    info[i] = [start, end]

# 부모 노드를 저장할 리스트 선언 및 초기화
parent = [i for i in range(n + 1)]

# rank를 저장할 리스트 선언 및 초기화
rank = [0 for i in range(n + 1)]

# 사이클 발생 여부를 저장 할 변수 선언 및 초기화
cycle = False

# 사이클 발생 시킨 차례의 번호
result = 0

# 게임 시작
for i in range(1, m + 1):
    node1 = info[i][0]
    node2 = info[i][1]
    if find_parent(parent, node1) == find_parent(parent, node2):    # 사이클이 발생한 경우 종료
        cycle = True
        result = i
        break
    else:   # 사이클이 발생하지 않았다면 계속 게임 진행 -> (union) 합집합 수행
        union_parent(parent, node1, node2, rank)


if cycle:
    print(result)
else:
    print(0)



