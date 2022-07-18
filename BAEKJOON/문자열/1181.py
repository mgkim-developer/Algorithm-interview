import sys
# 처음에 n개의 단어가 주어진다고 입력받는 것은 input()으로 입력 받음
n = int(input())
list_word = []

# n의 범위가 1 <= n <= 20000 이므로 시간제한을 고려하여 데이터는 sys.stdin.readline().strip()로 입력받음
for i in range(n):
    word = sys.stdin.readline().strip()
    list_word.append(word)

# set으로 중복 제거
set_list_word = set(list_word)

# sort를 쓰기 위해서 set자료형을 list자료형으로 변환
list_set_list_word = list(set_list_word)

# default 값으로 sort()를 해주면 알파벳 순으로 정렬
list_set_list_word.sort()

#sort를 하는데 key = len 파라미터를 넣어주면 길이를 기준으로 정렬함
list_set_list_word.sort(key = len)

for i in range(len(list_set_list_word)):
    print(list_set_list_word[i])