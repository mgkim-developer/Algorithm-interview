def num_sum(n,a):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]

    result = print(sum)
    return result

n = int(input())
a = list(map(int, input()))

num_sum(n, a)

