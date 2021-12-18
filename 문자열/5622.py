a = list(map(str, input()))
b = []  # a를 아스키코드로 바꿔서 담을 빈 리스트
c = []  # 각 문자를 0~9 중 해당하는 것으로 변환
for i in range(len(a)):
# 알파벳 대문자 아스키코드는 65~90
    for j in range(65, 91):
        if ord(a[i]) == j:
            b.append(j)
for k in range(len(b)):
    if b[k] == 65 or b[k] == 66 or b[k] == 67:
        c.append(2)
    elif b[k] == 68 or b[k] == 69 or b[k] == 70:
        c.append(3)
    elif b[k] == 71 or b[k] == 72 or b[k] == 73:
        c.append(4)
    elif b[k] == 74 or b[k] == 75 or b[k] == 76:
        c.append(5)
    elif b[k] == 77 or b[k] == 78 or b[k] == 79:
        c.append(6)
    elif b[k] == 80 or b[k] == 81 or b[k] == 82 or b[k] == 83:
        c.append(7)
    elif b[k] == 84 or b[k] == 85 or b[k] == 86:
        c.append(8)
    elif b[k] == 87 or b[k] == 88 or b[k] == 89 or b[k] == 90:
        c.append(9)

time = int(len(c))  # 1을 걸려면 2초가 필요하고 그이후 한칸 옆에 있는 숫자를 걸기위해선 1초씩 더걸리므로, 문자의 갯수가 n개면 n초를 초기에 추가해서 시간을 설정 해 줌으로서 한칸당 1초로 계산할 수 있게함

for l in range(len(c)):
    for m in range(1, 10):
        time = time + 1
        if c[l] == m:
            break

print(time)





