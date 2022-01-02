'''
 걸어서 가장 짧은 거리에 있는 방 선호
 각 층에 w개의 방이 있는
 h층건물임
 방번호는 yxx나 yyxx형태인데 여기서 Y나 YY는 층 수를 나타냄, XX는 엘레베ㅐ이터부터 세었을때의 번호를 나타낸다.
 걷는거리가 같을 때는 아래층의 방을 더 선호한다.
 N번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램을 짜야한다.
 첫번째 손님은 101호, 두번째 손님은 201호 등고 같이 배정한다.
 입력으로는
 케이스수
 높이, 층당객실수, 몇번쨰손님인지
 가 주어진다.
 각 케이스의 n번째 손님에게 배정되어야 하는 방번호 출력
'''

case = int(input())

for i in range(case):
    h, w, n = map(int,input().split())
    hotel = [[0] * w for _ in range(h)]  # 입력값 초기화
    # print(hotel)
    i = 0
    for j in range(h):
        i = (j+1)*100
        for k in range(w):
            hotel[j][k] = i+k+1 # 호텔객실번호 저장해서 list로 생성 (하지만 hotel의 row인덱스를 뒤집어야 진짜 hotel 객실 번호임 하지만 번호 지정해줄때부터 뒤집어서 생각하면 문제없음.)

    # real_hotel = [[0] * len(hotel[0]) for _ in range(len(hotel))]   # 180도 돌려서 초기화화
    #
    # for e in range(len(hotel)):
    #     real_hotel[e] = hotel[-e-1]

    # print(hotel)
    # print(real_hotel)

    # hotel 객실번호를 101,201,301 의 순서로 탐색하여 n번째에 해당하는 객실번호 출력
    if n > h and n % h != 0:
        floor = (n % h) - 1
        sequence = (n // h)
        # print(n/h)
        # print(1)
    elif n > h and n % h == 0:
        floor = h - 1
        sequence = (n // h) - 1
        # print(2)
    elif n == h:
        floor = h - 1
        sequence = 0
        # print(3)
    elif n < h:
        sequence = 0
        floor = (n % h) - 1
        # print(4)
    print(hotel[floor][sequence])

