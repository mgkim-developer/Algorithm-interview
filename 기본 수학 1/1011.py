"""
문제 접근

장치를 처음 작동시키면 -1, 0, 1만큼 이동가능
사실상 음수 혹은 0 거리만큼의 이동은 의미가 없음. 따라서 1만큼 이동하는 것이라고 볼 수 있음
그다음은 0, 1, 2 만큼 이동가능 여기서 2만큼 이동했으면
그다음 시기에는 1, 2, 3만큼 이동 가능

이전 작동시기에 k광년을 이동하였을 때는, k-1, k, k+1 만큼 이동 가능.
y지점에 도착하기 바로 직전의 이동거리는 반드시 1
x 지점부터 y지점으로 이동하는데 필요한 횟수의 최솟값은?

입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다.
각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며,
x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

예제 입력 1
3
0 3
1 5
45 50

예제 출력 1
3
3
4

"""

import sys

case = int(sys.stdin.readline())
for i in range(case):
    x, y  = map(int, sys.stdin.readline().strip().split())
    # print(x, y)
    distance = y-x
    list = []
    num = 0
    count = 0
    ss = 0
    for j in range(1, distance + 1):
        for k in range(1, distance + j):
            ran = j ** 2
            if k == ran:
                # print(ran)
                num = num + 2
                list.append(num-1)
                s = j
                ss = k
            else:
                pass
    # print(list)
    # print(ss)
    # for l in range()
    if ss - s + 1 <= distance <= ss + s:
        # print(ss - s + 1,distance, ss + s)

        if ss < distance:
            count = list[-1]+1
            print(count)
        elif distance <= ss:
            count = list[-1]
            print(count)
    else:
        pass