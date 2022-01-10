m = int(input())
n = int(input())

# 출력은 첫번쨰 줄에는 해당 범위 내의 소수의 합
#  두번쨰 줄에는 해당 범위 내의 소수 중에 최솟값

prime_range = n - m
# print(prime_range)

natural_list = [i for i in range(m, n + 1)]
print(natural_list)

import math

# 소수 판별 함수 작성
def find_prime_num(n): # n까지의 소수를 찾는 함수
    prime_num = [i for i in range(n + 1)]
    for j in range(2, int(math.sqrt(n))+1):
        for l in prime_num:
            if l / j == 1: # 자기 자신으로 나뉘는 것은 제외
                pass
            elif l % j == 0: # 그 이외에 나뉘는 수가 존재하면
                prime_num.remove(l) # 그 수는 소수 리스트에서 제거
    # print(prime_num)

    return prime_num

prime_num_list = find_prime_num(n)
print(prime_num_list)

# print(natural_list)

result = natural_list

for k in natural_list:
    # print(natural_list)
    print(k)
    # if k not in prime_num_list:
    #     natural_list.remove(k)
    # else:
    #     pass

if len(natural_list) == 0:
    print(-1)
else:
    print(natural_list)


61, 67, 71, 73, 79, 83, 89, 97

