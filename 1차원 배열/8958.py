import sys

n = int(input())    # 입력받을 케이스 갯수 입력받기
for i in range(n):
    k = list(map(str, sys.stdin.readline().strip())) # 케이스 입력받아서 리스트로 저장
    count = 0
    ccount = 0
    for j in range(len(k)):
        if k[j] == 'O':
            count = count + 1   #연속된 'O'일 경우 'O' 에 대한 점수를 1점씩 증가시킴
            ccount = ccount + count # 1씩 증가시킨 점수를 합산해줌
        else:
            count = 0   # 'X'가 나오면 "O"에 대한 점수는 다시 1점부터 시작하도록 설정

    print(ccount)