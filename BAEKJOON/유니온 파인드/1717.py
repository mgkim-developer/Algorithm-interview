'''
초기화 n + 1개의 집합 {0}, {1}, ..., {n}이 있다.
이 집합에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성할 것.

- 입력 조건
첫째 줄에 n, m이 주어진다.
이때 n은 0~n까지의 초기 집합이 주어짐을 의미.
m은 입력으로 주어지는 연산의 개수임.

합집합은 0 a b 의 형태로 주어지고,
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어짐

- 출력 조건
1로 시작하는 입력에 대해서는 a와 b가 같은 집합에 포함되면 "YES" 또는 "yes" 그렇지 않다면 "NO", 또는 "no"를 한 줄에 하나씩 출력


i)
find_parent 함수와
union_parent 함수를 작성하면 될 것으로 판단된다.
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

    # union-by-rank 최적화 적용
    # rank가 더 큰 트리에 작은 트리를 붙인다
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:   # 만약 rank가 같다면 임의로 rootX트리에 rootY트리를 붙인다.
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1   # rootX 트리의 높이를 +1


n, m = map(int, input().split())
# 초기 집합
arr = [i for i in range(n + 1)]
# 주어진 연산
expression = [[] for i in range(m)]
for i in range(m):
    # a는 연산의 종류, b와 c는 연산의 대상 원소
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    expression[i] = [a, b, c]

# parent 리스트 선언 및 초기화
parent = [0 for i in range(n + 1)]
for i in range(n + 1):
    parent[i] = i

# rank 리스트 선언 및 초기화
rank = [0 for i in range(n + 1)]

for i in range(m):
    what, a, b = expression[i]
    if what == 0:
        union_parent(parent, a, b, rank)
    elif what == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')