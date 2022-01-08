case = int(input())
list = list(map(int, (input().split())))
prime_number = []

for i in range(case):
    count = 0   # 소수는 1과 자기자신으로만 나뉘는 수이다. 즉 count가 2이면 소수로 판별할 예정
    for j in range(1, list[i]+1):
        rest = list[i]%j
        if rest == 0 :
            count = count + 1
        else:
            pass
    if count == 2:
        prime_number.append(list[i])

print(len(prime_number))