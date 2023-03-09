# 그리디
n = 1260
cnt = 0

coin = [500, 100, 50, 10]

for c in coin:
    cnt  = cnt + (n // c)
    n = n % c

print(cnt)