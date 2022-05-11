a, b = map(int, input().split())
if a == 0 and b < 45:
    m = 60 * 24 + b
    em = m -45
    rh = em // 60
    rm = em % 60
    print(rh, rm)
elif a == 0 and b >= 45:
    rh = 0
    rm = b -45
    print(rh, rm)
else:
    m = a * 60 + b
    em = m - 45
    rh = em // 60
    rm = em % 60
    print(rh ,rm)
