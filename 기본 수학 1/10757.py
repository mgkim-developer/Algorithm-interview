import sys

a, b = map(int, sys.stdin.readline().strip().split())
print(a+b)


#-------------아래 코드에 반례있음 12, 34 같이 작은 수의 합의 반례---------
# import sys
# a, b = sys.stdin.readline().rstrip().split()
# a1 = a[:-int(len(a)/2)]
# a2 = a[-int(len(a)/2):]
# b1 = b[:-int(len(a)/2)]
# b2 = b[-int(len(a)/2):]
# c1 = int(a1)+int(b1)
# c2 = int(a2)+int(b2)
# c1 += int(str(c2)[:-len(b2)])
# c2 = int(str(c2)[-len(b2):])
# c = str(c1)+str(c2)
# print(c)