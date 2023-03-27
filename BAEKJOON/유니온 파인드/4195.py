'''
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
이때, 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

- 입력
첫째 줄에 테스트 케이스의 개수 주어짐.
각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어짐 (F <= 100,000)
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.(친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대소문자로 이루어진 길이 20이하의 문자열)

- 출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있지 구하는 프로그램 작성

i)
일단 문자열을 공백을 기준으로 입력받아서 저장하고,
유니온을 해준다. 그러면 두 사용자는 친구관계로 인식할 수 있다. root가 같을 것이기 때문이다. 같은 root를 가진 사람이 몇명 있는지 반환하면 될 것이다.

주의할 점이 있다.
숫자가 아닌 문자열 입력을 받기 때문에,
기존 유니온 파인드와 구조는 거의 같지만, 딕셔너리를 이용하여 문제를 해결해야 할 것으로 보인다.

또한 각 뿌리 노드로부터 구성된 트리의 크기를 알아야 하기 때문에 network 라는 딕셔너리를 하나 더 만들어서 사용할 것이다.

root 노드가 같은 입력이 들어올 경우에도 크기를 출력해야 한다.
그리고 우리가 출력해야 하는 것은 트리의 깊이가 아니라, 트리에 속한 노드 개수이다.
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)  # x의 루트노드를 찾아서 a에 저장
    b = find_parent(parent, y)  # y의 루트노드를 찾아서 b에 저장
    if a == b:  # a == b 이면 이미 친구이므로 따로 network에 추가하지 않고 그대로 network[a] 또는 network[b]를 반환
        return network[a]
    elif a > b: # a가 b보다 알파벳순으로 뒤에 있으면
        parent[a] = b   # parent[a]의 value를 b로 저장
        network[b] = network[b] + network[a]    # b의 친구네트워크 수에다가 a의 친구 네트워크 수도 더해줌
    else:
        parent[b] = a   # parent[b]의 value를 a로 저장
        network[a] = network[a] + network[b]    # a의 친구 네트워크 수에다가 b의 친구 네트워크 수도 더해줌

t = int(input())

for i in range(t):
    parent = dict()     # dict형으로 선언
    network = dict()    # dict형으로 선언

    f = int(input())

    for j in range(f):
        x, y = sys.stdin.readline().rstrip().split()

        if x not in parent: # x가 parent에 key로 없으면
            parent[x] = x   # parent에 key값과 value값을 자기자신으로 초기화 하여 저장
            network[x] = 1  # 그리고 network의 자신의 key값에 1을 value로 저장
        if y not in parent: # y가 parent에 key로 없으면
            parent[y] = y   # parent에 key값과 value값을 자기자신으로 초기화 하여 저장
            network[y] = 1  # 그리고 network의 자신의 key값에 1을 value로 저장
        union_parent(parent, x, y)  # 친구 네트워크 형성(union 해줌)
        print(network[find_parent(parent, x)])

