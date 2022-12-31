# n의 피보나치수
n = int(input())

# 재귀방식으로 피보나치 구현
def recursion_fibo(num):
    if num == 1 or num == 2:
        return 1
    return recursion_fibo(num - 1) + recursion_fibo(num - 2)

print(recursion_fibo(n), end=" ")



# 바텀업 방식으로 DP테이블 만들어서 다이나믹 프로그래밍으로 피보나치 구현
def dynamic_fibo(num):
    # 한 번 계산된 결과를 메모이제이 하기위한 리스트 초기화
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    dynamic_fibo_count = 0
    # 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
    for i in range(3, n + 1):
        dynamic_fibo_count = dynamic_fibo_count + 1
        d[i] = d[i - 1] + d[i - 2]

    return dynamic_fibo_count

print(dynamic_fibo(n))