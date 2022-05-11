n = int(input())  #과목 개수 입력받기

l = list(map(int, input().split())) #과목당 점수 입력받기

# 최고점 찾기
max_score = l[0]
for i in range(len(l)):
    if max_score <= l[i]:
        max_score = l[i]
    else:
        pass

result = [] #새로 계산한 점수값 저장할 빈 리스트 생성

for j in range(len(l)):
    result.append(l[j]/max_score*100)

# 새로 계산한 점수값들의 평균 계산
m = 0
for k in range(len(result)):
    m = m + result[k]
print(m/(len(result)))

