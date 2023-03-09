'''
N종류의 동전을 가지고 있다. 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만드려고 한다.
이때 필요한 동전 개수의 최솟값을 구하라.

입력으로는
첫째 줄에 N과 K가 주어지고, (1 < N <10, 1 <= k <= 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 A_i가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

i)
동전의 가치가 오름차순으로 주어지므로,
해당 데이터를 리스트에 담고, 가장 큰 것부터 사용하여 목표금액을 나눠준다.
그리고 해당 몫을 coin_count라는 변수에 저장하고,
그다음 크기의 동전으로 나머지를 나눠준다.
그리고 해당 몫을 coin_count라는 변수에 더해준다.
이것을 반복하여 더이상 나누어지지 않을 때, 즉 나눌 값이 0이 되었을 때의 coin_count를 반환하면 될 것 이다.
'''
import sys

n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_count = 0
remain = k
while remain != 0:
    now_coin = coin_list.pop()
    quotient = k // now_coin
    coin_count = coin_count + quotient
    remain = k % now_coin
    k = remain

print(coin_count)
