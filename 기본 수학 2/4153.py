import sys

a = 1
while True:
    length = list(map(int,sys.stdin.readline().split()))
    if length[0] == 0:
        break
    # print(length)
    length.sort()
    # print(length)
    if (length[0])**2 + (length[1])**2 == (length[2])**2:
        print("right")
    else:
        print("wrong")