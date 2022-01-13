
# 에라토스테네스의 체 알고리즘 이용
import sys
import math
# 2부터 num까지의 모든 수에 대하여 소수 판별
num = 123456
# 처음에는 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
array = [True for i in range(num+1)]
# print(array)

for i in range(2, int(math.sqrt(num))+1):
    if array[i] == True:    # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= num:
            array[i * j] = False
            j = j + 1

# print(array)

#소수를 담을 prime_list 라는 이름의 리스트 생성
prime_list = []
for i in range(2, num+1):
    if array[i]:
        prime_list.append(i)

# print(prime_list)

while True:
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    two_n = n * 2
    search_range = []
    for i in range(n+1, two_n + 1):
        search_range.append(i)
    for j in search_range:
        if j in prime_list:
            count = count + 1
    print(count)
