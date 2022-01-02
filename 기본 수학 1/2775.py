"""
아파트에는 거주조건이 있음.
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다"
비어있는 집은 없고, 모든 거주민들이 이 계약조건을 지키고 있다.
주어지는 양의정수 k와 n에 대해 k층 n호에는 몇명이 살고있는지 출력하라.
아파트에는 0층부터 있고, 1호부터 있음
0층의 i호에는 i명이 산다.

입력의 첫번쨰 줄에는 test case의 수
그리고 각케이스마다 첫번째줄에는 정수k, 두번째 줄에는 정수n이 주어짐.

# 각 층에대한 대략적인 계산
#
# 1 4 10            (2층)
# 1 3 6 10          (1층)
# 1 2 3 4 5 6 7 8 9 (0층)

"""

test_case = int(input())

for i in range(test_case):
    k = int(input())
    n = int(input())
    people = [[0] * 14 for _ in range(k+1)] # 초기화
    # print(people)
    for j in range(14):
        people[0][j] = j+1  # 0층은 1호는 1명, 2호는 2명, 3호는 3명... 이므로 초기값 설정
    # print(people)
    for u in range(1, k+1): # 0층을 기준으로 연산을 수행해야 하므로 range범위를 1 ~ k+1로 설정함
        for y in range(14): # 호수의 인덱스는 1호~14호까지이지만 0~13으로 설정
            plus = people[0][y]     # plus는 계속해서 더해져야하는 누적값을 의미하며 각 호수의 초기값은 0층을 기준으로함
            for p in range(u):
                for o in range(y):
                    # print(o)
                    plus = plus + people[p][o]
            people[u][y] = plus
    # print(people)
    # print(k)
    # print(n)
    print(people[k][n-1])   # 층은 0층부터 존재하므로 인덱스가 동일하지만, 호수의 경우에는 1호부터 14호까지이므로 인덱스값을 맞춰주기 위해서는 -1을 해주어야함.



