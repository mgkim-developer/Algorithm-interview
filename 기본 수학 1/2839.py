"""
문제접근

입력을 n 으로 받고, 봉지 갯수를 세기위한 count 변수 생성
n이 0이 될 때까지 반복
5kg봉지와 3kg 봉지로 나누어 담는데, 봉투를 최소로 사용해야 함.
n을 5로 나눈 나머지가 0이 되면, count에 5로나눈 몫을 더해주고, 나누어 떨어지지 않는다면,
n에서 3을 빼고 count에 +1을한다.

5와 3으로 완벽히 나누어 담지 못하면, -1을 출력
"""
n = int(input())

count = 0
while n >= 0 :
    if n % 5 == 0:
        count = count + (n // 5)
        print(count)
        break
    n = n - 3
    count = count + 1
else:
    print(-1)