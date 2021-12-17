def find_alpha(a):

    alpha = []
    base = [] #초기화 선언
    for i in range(97, 123):
        alpha.append(chr(i))


    for j in range(len(alpha)):
        base.append(-1)


    ascii_alpha = []
    for m in range(len(alpha)):
        ascii_alpha.append(ord(alpha[m]))


    for k in range(len(a)):
        if ord(a[k]) in ascii_alpha:
            index = ascii_alpha.index(ord(a[k]))
        else:
            pass

        if base[index] == -1:
            base[index] = k

    for b in range(len(base)):
        print(base[b], end=' ')


    return



a = list(map(str, input()))
find_alpha(a)



# k 가 1일때 b 이고 -> 아스키로바꾸고 alpha(현재는 아스키가아니라 문자임)에서 해당 아스키같은것에 k대입
# alpha를 아스키로변환하고