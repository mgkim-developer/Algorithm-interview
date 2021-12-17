def find_alpha(a):
    alpha = []
    for j in range(26):
        alpha.append(-1)    # 알파벳이 단어에 포함되어 있지 않다면 -1을 출력해야 하므로, 초기화를 -1로 시켜줌
    for i in range(len(a)): # 입력 문자열을 인덱스 차례대로 어떤 소문자인지 확인 후, 해당 인덱스를 alpha리스트와 일치하는 소문자의 인덱스에 삽입
        if a[i] == 'a' and alpha[0] == -1:  # 같은 알파벳이 중복해서 존재해도, 최초 나왔던 인덱스를 입력해주어야 하기 때문에, and alpha[0] == -1 조건이 필요함
            alpha[0] = i
        elif a[i] == 'b' and alpha[1] == -1:
            alpha[1] = i
        elif a[i] == 'c' and alpha[2] == -1:
            alpha[2] = i
        elif a[i] == 'd' and alpha[3] == -1:
            alpha[3] = i
        elif a[i] == 'e' and alpha[4] == -1:
            alpha[4] = i
        elif a[i] == 'f' and alpha[5] == -1:
            alpha[5] = i
        elif a[i] == 'g' and alpha[6] == -1:
            alpha[6] = i
        elif a[i] == 'h' and alpha[7] == -1:
            alpha[7] = i
        elif a[i] == 'i' and alpha[8] == -1:
            alpha[8] = i
        elif a[i] == 'j' and alpha[9] == -1:
            alpha[9] = i
        elif a[i] == 'k' and alpha[10] == -1:
            alpha[10] = i
        elif a[i] == 'l' and alpha[11] == -1:
            alpha[11] = i
        elif a[i] == 'm' and alpha[12] == -1:
            alpha[12] = i
        elif a[i] == 'n' and alpha[13] == -1:
            alpha[13] = i
        elif a[i] == 'o' and alpha[14] == -1:
            alpha[14] = i
        elif a[i] == 'p' and alpha[15] == -1:
            alpha[15] = i
        elif a[i] == 'q' and alpha[16] == -1:
            alpha[16] = i
        elif a[i] == 'r' and alpha[17] == -1:
            alpha[17] = i
        elif a[i] == 's' and alpha[18] == -1:
            alpha[18] = i
        elif a[i] == 't' and alpha[19] == -1:
            alpha[19] = i
        elif a[i] == 'u' and alpha[20] == -1:
            alpha[20] = i
        elif a[i] == 'v' and alpha[21] == -1:
            alpha[21] = i
        elif a[i] == 'w' and alpha[22] == -1:
            alpha[22] = i
        elif a[i] == 'x' and alpha[23] == -1:
            alpha[23] = i
        elif a[i] == 'y' and alpha[24] == -1:
            alpha[24] = i
        elif a[i] == 'z' and alpha[25] == -1:
            alpha[25] = i
        else:
            pass
    return alpha

def alpha_print(alpha):
    for k in range(len(alpha)):
        print(alpha[k], end = ' ')
    return



a = list(map(str, input()))
a = find_alpha(a)
alpha_print(a)
