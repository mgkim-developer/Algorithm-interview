# 인풋값을 ord로 받고
# ord 시작점인 a의 ord를 구함
#
# 그리고 이제 한줄로 a~인풋값을 프린트해야한다.
#
# 그러면 ord(a)부터 ord(인풋값)까지 반복문으로 프린트 하면 되지 않을까?

x = input()
x = str(x)
a = str('a')
ordx = ord(x)
orda = ord(a)

while orda <= ordx:
    print(chr(orda), end = ' ')
    orda = orda + 1



