d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(19) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기
  for j in range(19) :
    d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)-1][int(y)-1] = 1

for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print()
