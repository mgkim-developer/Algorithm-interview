a = int(input(), 16)
for i in range(1, 16):
    answer = a * i
    print("%X*%X=%X" %(a, i, answer))
