from collections import Counter #리스트에 있는 요소의 최빈값을 구하기 위한 라이브러리

a = input()

# 리스트에 들어있는 문자들의 변수를 생성해 주고, 해당 단어를 인덱스 루프돌면서 해당하는 문자변수 카운트 +1해주고, 마지막에 문자변수값이 가장 큰 것을 대문자로 출력
# 65~90은 소문자
# 97~122는 대문자이고 소문자와 대문자의 차이난 32
b = []  # 입력값을 대문자의 아스키코드로 바꿔 저장할 리스트생성.

for i in range(len(a)):
    for j in range(65, 91):
        if ord(a[i]) == j or ord(a[i]) == j+32: # 입력 값 중 소문자가 존재하므로 소문자가 대문자의 아스키코드로 저장되도록 ord(a[i]) == j+32
            b.append(j)
        else:
            pass

cnt = Counter(b)    # b의 요소값들의 빈도를 딕셔너리로 반환
most = cnt.most_common()    # b의 요소값들의 빈도를 튜플로 반환

if len(most) != 1:  #대소문자 구별을 하지 않을 때, 1가지 문자로만 구성된 문자열이 존재 할 수 있으므로, 해당 케이스를 고려
    if most[0][1] != most[1][1]:    # 빈도가 같은 문자가 존재 할 시, ?를 출력해야 하므로 조건식 작성
        print(chr(most[0][0]))
    else:
        print("?")
else:
    print(chr(most[0][0]))  #결과를 출력 할 때는 아스키코드를 다시 문자로 바꾸어 출력