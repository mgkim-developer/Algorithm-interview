
# 에라토스테네스의 체 알고리즘 이용
import sys
import math
# 2부터 nnum까지의 모든 수에 대하여 소수 판별
num = 123456
nnum = 246912
# 처음에는 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
array = [True for i in range(nnum+1)]
# print(array)

for i in range(2, int(math.sqrt(nnum))):
    if array[i] == True:    # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= nnum:
            array[i * j] = False
            j = j + 1


while True:
    n = int(sys.stdin.readline())
    two_n = n * 2
    count = 0
    if n == 0:
        break

    for i in range(n+1, two_n + 1):
        if array[i] == True:
            count = count + 1
    print(count)
