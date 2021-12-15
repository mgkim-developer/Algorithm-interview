# 셀프넘버가 아닌 것들을 담을 리스트 빈 리스트 생성
a = []

# 재귀 함수를 이용하여 셀프넘버가 아닌 것을 계산하여 리스트 a에 담아 주기
def self(i):
    if i < 10001:
        #이떄, zfill을 이용하여 5자리를 맞춰주는 것이 핵심
        j = str(i).zfill(5)
        sum = i + int(j[0]) + int(j[1]) + int(j[2]) + int(j[3]) + int(j[4])
        i = sum
        a.append(sum)
        self(i) #self(i)값이 다시 self함수의 i값으로 들어가도록 설정 (재귀)
    else:
        return
# 1~10000까지 셀프넘버가 아닌 것들을 self함수를 반복시켜서 리스트 a에 저장
for i in range(1, 10001):
    self(i)

# 중복값을 제거 해주기 위해 set 이용
e = set(a)

# 다시 리스트로 만들어 주기
a = list(e)

# 오름차순으로 정렬
a.sort()

# 1~10000 숫자를 담을 빈 리스트 생성
b = []
# 리스트 b에 1~10000 담기
for k in range(1, 10001):
    b.append(k)

# 1~10000을 담은 리스트 b에서 셀프넘버가 아닌 것들을 모아놓은 리스트 a에 없는 원소들만 리스트 d에 담아주기
d = [q for q in b if q not in a]

# 리스트 d의 원소를 차례대로 출력하기
for g in d:
    print(g)

