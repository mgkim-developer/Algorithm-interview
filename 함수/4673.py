# a = []
# def _self(i):
#   if i < 10001:
#    j = str(i).zfill(5)
#    _sum = i + int(j[0]) + int(j[1]) + int(j[2]) +int(j[3]) + int(j[4])
#    i = _sum
#    a.append(_sum)
#    _self(i)
#   else:
#     return a
#
# for i in range(1,10001):
#   _self(i)
#
# e = set(a)
# a = list(e)
# a.sort()
#
# b= []
# for k in range(1,10001):
#   b.append(k)
#
# d = [item for item in b if item not in a]
# for h in d:
#   print(h)

import sys
sys.setrecursionlimit(10000)

def self():
    a = []
    b = []
    for i in range(1, 10001):
        a.append(i)

    for j in range(len(a)):
        if a[j] == 1:
            b.append(a[j])
        elif 1 < a[j] <= 9:
            if a[j-1] + a[j-1] not in b:
                # if a[j] not in b:
                b.append(a[j])
                # else:
                #     pass
            else:
                pass


        # elif 10 <= a[j] <= 99:
        #
        # elif: 100 <= a[j] <= 999:
        #
        # elif:  1000 <= a[j] <= 9999
        #     #     a[j]+a[j]//10+a[j]%10 not in b:
        #     # b.append(a[j])
        # elif: a[j] == 10000:

        else:
                pass

    print(b)
    return

self()