def fool_math(a):
    one = a[0][2] + a[0][1] + a[0][0]
    two = a[1][2] + a[1][1] + a[1][0]
    if one > two:
        print(int(one))
    else:
        print(int(two))

    return

a = list(map(str, input().split()))

fool_math(a)
