'''
        n 은 vertices 의 갯수이고, 각 노드는 0 ~ n-1 의 번호가 할당 되어있음
        edges[i] = [ai, bi] 이고, 이는 edges[i] 가 노드 a 와 노드 b 가 연결된 간선을 의미함.
        반환으로는 complete connected components 의 갯수를 반환해야한다.
        그렇다면 주어진 데이터를 이용하여 complete connected components 의 갯수를 찾는 것이 핵심일 것이다.

        complete connected components 란 무엇일까?
        예시 그림을 보면 쉽게 파악할 수 있다.

        각 부분 그래프의 모든 노드가 서로 연결되어야 한다.

        그러면 주어진 데이터를 이용하여 모든 노드에 대해 DFS 또는 BFS 를 수행하여
        각 부분 그래프를 구한 후, 해당 부분 그래프에 속한 노드의 갯수를 v 라고 하고, 간선의 갯수를 e 라고 할 때,
        complete connected components 인 경우 가져야하는 노드의 갯수를 구하여 비교하면 될 것이다.
        노드 갯수가 m 개인 경우, 가져야하는 간선의 갯수는 m(m-1)/2 개 이다.

        비교해서 간선의 갯수가 동일할 경우, complete connected components 로 판단하면 된다.
        '''

from collections import deque


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # 노드의 갯수
        print("n : input vertices num =", n)

        # 주어진 간선들
        print("edges : input edges list = ", edges)
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            node_a, node_b = edges[i]
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)
        print("graph = ", graph)

        # 노드의 방문 여부를 기록할 리스트
        visited = [False] * (n + 1)
        print("visited = ", visited)

        # BFS 를 수행할 때 사용할 큐
        q = deque()
        print("q = ", q)

        # 결과를 반환할 result 변수
        result = 0

        # BFS 함수 정의
        def bfs(graph, start, visited):
            # 생성된 서브 그래프의 노드를 저장할 리스트
            sub_graph_node = []
            q.append(start)
            sub_graph_node.append(start)
            visited[start] = True
            while q:
                now = q.popleft()
                print("now", now)
                for next in graph[now]:
                    if not visited[next]:
                        visited[next] = True
                        q.append(next)
                        sub_graph_node.append(next)

            print("sub_graph_node = ", sub_graph_node)

            # 서브 그래프에 포함된 간선의 갯수를 저장할 변수
            sub_graph_components_edge = 0
            for i in sub_graph_node:
                sub_graph_components_edge = sub_graph_components_edge + len(graph[i])
            # 그래프에 노드 정보를 저장할 때 양방향으로 저장했기 때문에 // 2 를 해줌
            sub_graph_components_edge = sub_graph_components_edge // 2
            print("sub_graph_components_edge = ", sub_graph_components_edge)

            # 서브 그래프에 포함된 노드의 갯수를 저장할 변수
            m = len(sub_graph_node)
            print("sub_graph_node 의 갯수 m = ", m)

            # 노드의 갯수가 m 개 일때, complete_connected_coponents 가 가지는 정상적인 간선 갯수를 구하는 공식
            normal_complete_connected_components = (m * (m - 1)) // 2
            # 만약 직접 구한 서브 그래프의 간선의 갯수가 normal_complete_connected_components 와 일치하면 return True
            if sub_graph_components_edge == normal_complete_connected_components:
                return True

        # 모든 노드에 대해 BFS 수행
        for i in range(n):
            if visited[i] == False:
                start = i
                if bfs(graph, start, visited) == True:
                    result = result + 1

        return result