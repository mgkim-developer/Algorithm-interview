'''
골드바흐의 추측은 유명한 정수론의 미해결 문제다.
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다.
그리고, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
ex) 4 = 2 + 2, 6 = 3 + 3 등이다.
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보타 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.

만약 가능한 n의 골드바흐 파틴션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력 할 것.

입력조건 : 첫째줄에는 테스트케이스의 개수가 주어짐. 각 테스트 케이스는 한줄로 이루어져 있고, 짝수 n이 주어짐

이떄, n은 4 <= n <= 10000

출력 조건 : 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력, 출력하는 소수는 작은 것부터 먼저 출력, 그리고 그 사이는 공백으로 구분.
'''

# 에라토스테네스의 체 알고리즘을 이용하여 10000 까지의 소수 찾기
import sys
import math
n = 10000
# 처음엔 모든 수가 소수(True)인 것으로 초기화
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하여
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:    # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j = j + 1

# print(array)

prime_num = []
for i in range(2, len(array)):
    if array[i] == True:
        prime_num.append(i)


# print(prime_num)


# 소수 둘을 정하고 합이 n이 되는지 보는 것 O(N^2)
# n에서 어떤 소수를 뺀 값이 소수인지 확인하는 것 O(N*logN)

''' 처음에는 시간복잡도 N^2의 방법으로 풀었는데, time complexity 문제로 오답처리 받음
추후 time compeelxity를 고려해서 n에서 어떤 소수를 뺸 값이 소수인지 확인하는 방법으로 재풀이 하여 정답처리 완료.
시간복잡도를 고려해서 작성하는 습관을 들 것.
'''


case = int(input())

for i in range(case):
    number = int(sys.stdin.readline())
#--------------------- n에서 어떤 소수를 뺀 값이 소수인지 확인하는 것 O(N*logN)
    result = []
    for j in prime_num:
        if number - j in prime_num:
            result.append(j)
            result.append(number-j)
    # print(result)
    difference = result[1] - result[0]
    final_result = []
    for l in range(0, len(result), 2):
        a = result[l]
        b = result[l+1]
        # print(a)
        # print(b)
        if a - b <= difference:
            difference = b - a
            final_result.append(a)
            final_result.append(b)
        else:
            pass

        # print(difference)
        # print(final_result)
    print(final_result[-1], final_result[-2])

#---------------------------------소수 둘을 정하고 합이 n이 되는지 보는 것 O(N^2)
    # # print(type(number))
    # # print(number)
    # # a = number//2
    # # b = number//2
    # result = []
    # for j in prime_num:
    #     # print(j)
    #     for k in prime_num:
    #         # print(k)
    #         if k + j == number:
    #             result.append(j)
    #             result.append(k)
    #             break
    # print(result)
    # difference = result[1] - result[0]
    # final_result = []
    # for l in range(0, len(result), 2):
    #     a = result[l]
    #     b = result[l+1]
    #     # print(a)
    #     # print(b)
    #     if a - b <= difference:
    #         difference = b - a
    #         final_result.append(a)
    #         final_result.append(b)
    #     else:
    #         pass
    #
    #     # print(difference)
    #     # print(final_result)
    # print(final_result[-1],'', final_result[-2])