# 에라토스테네스의 체를 이용한 1978번 풀이
'''
에라토스테네스의 체 알고리즘 동작과정
1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
4. 더이상 반복할 수 없을 떄까지 2번과 3번의 과정을 반복한다.
'''



# 에라토스테네스의 체 알고리즘(python)
def find_prime_number(a):
    import math
    # 2부터 a까지의 모든 수에 대하여 소수 판별
    # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    array = [True for i in range(a + 1)]

    # 에라토스테네스의 체 알고리즘 수행
    # 2부터 n의 제곱근까지의 모든 수를 확인하여
    for i in range(2, int(math.sqrt(a)) + 1):
        if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= a:
                array[i * j] = False
                j = j + 1

    # 모든 소수 출력
    prime_num_list = []
    for i in range(2, a + 1):
        if array[i]:
            # print(i, end=' ')
            prime_num_list.append(i)
    # print(prime_num_list)
    # print(type(prime_num_list))

    case = int(input())
    list_input = list(map(int, input().split()))
    # print(list)

    count = 0
    for k in list_input:
        if k in prime_num_list:
            count = count + 1

    print(count)

prime_num = find_prime_number(1000)



