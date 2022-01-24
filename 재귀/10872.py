'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력 1
10
예제 출력 1
3628800
예제 입력 2
0
예제 출력 2
1
'''

# 재귀함수를 이용한 코드
n = int(input())
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))


'''
n에 5를 입력했을 때,
재귀함수 실행과정
5 * factorial(4)
(5*4) * factorial(3)
(5*4*3) * factorial(2)
(5*4*3*2) * factorial(1)
(5*4*3*2*1)

'''

'''
# for문 이용한 코드
n = int(input())
def factorial(n):
    n_list = []
    n_fac = 1
    for i in range(1, n+1):
        n_fac = n_fac * i
    print(n_fac)

factorial(n)
'''
