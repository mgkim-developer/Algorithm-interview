import sys

# 테스트 갯수 입력받기
c = int(input())

# 첫 수로 학생의 수가 입력되고, 이어서 N 명의 점수를 입력받음
for i in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    s = 0 # 평균계산할 점수합산을 저장할 변수 생성
    for j in range(1,l[0]+1):   # 0번쨰 인덱스의 원소는 학생수 이기 떄문에 1부터 len(l)까지 range실행
        s = s + l[j]
    mean = s/(l[0]) # 해당 케이스의 평균을 구함

    count = 0
    for k in range(1, l[0]+1):   # 평균을 넘는 학생의 수를 count변수에 저장
        if l[k] > mean:
            count = count + 1
        else:
            pass
    # 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
    rate = (count / l[0]) * 100
    print("{:.3f}%".format(rate))
