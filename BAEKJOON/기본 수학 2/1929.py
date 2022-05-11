

m, n = map(int, input().split())
# print(m, n)

#-------------이렇게 작성하면 원소를 하나씩 확인 하는 것이기 때문에 시간초과를 피할 수 없음------------------------------------------
# natural_list = [i for i in range(m, n+1)]
# # print(natural_list)
#
# # prime_num = [l for l in range(n+1)]
# #
# for k in range(2, int(math.sqrt(n))+1):
#     for j in natural_list:
#         if j / k == 1: # 자기 자신으로 나뉘는 것은 제외
#             pass
#         elif j % k == 0: # 그 이외에 나뉘는 수가 존재하면
#             natural_list.remove(j)
#
# for o in range(len(natural_list)):
#     print(natural_list[o])


#----------------------------------에라토스테네스의 체 알고리즘을 이용한 풀이--------------------------------------------------
'''
에라토스테네스의 체 알고리즘 동작과정
1. 2부터 n까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
4. 더이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
'''

import math

# 2부터 n까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하여
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j = j + 1

# print(array)

# 모든 소수를 result 리스트에 저장
result = []
for i in range(2, n + 1):
    if array[i]:
        result.append(i)

# print(result)
# print(result[0])


for i in range(len(result)):
    if m <= result[i] and result[i] <= n:
        print(result[i])

