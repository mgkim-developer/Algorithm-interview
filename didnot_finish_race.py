# https://programmers.co.kr/learn/courses/30/lessons/42576
# 해시 - 완주하지 못한 선수

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    sub_participant = []
    for k in range(len(participant)):
        sub_participant.append(participant[k])
    # print(sub_participant)

    sub_completion = []
    for k in range(len(completion)):
        sub_completion.append(completion[k])
    # print(sub_completion)

    for i in participant:
        for j in range(len(completion)):
            # print(sub_participant)
            if completion[j] == i and i in sub_completion:
                sub_completion.remove(i)
                sub_participant.remove(i)
            else:
                pass

    for i in range(len(sub_participant)):
        answer = sub_participant[i]
    return answer


'''
프로그래머스는 백준처럼 print를 요구하는 것이 아니라
실행 후에 리턴값에 해당하는 변수에 값이 들어있기를 요구한다.
'''


# ---------------------------Sort/Loop을 사용한 문제풀이--------------------------------

def soulution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다.
    participant.sort()
    completion.sort()

    # 2. completion list의 len만큼 participant를 찾아서 없는 사람을 찾는다.
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant) - 1]


# ---------------------------Hash를 사용한 문제풀이---------------------------------------

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.

    return hashDict[sumHash]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))


# ---------------------------Counter를 사용한 문제풀이---------------------------------------

import collections
def solution(participant, completion):
    # 1. participant의 Counter를 구한다.
    # 2. completion의 Counter를 구한다.
    # 3. 둘의 차를 구하면 정답만 남아있는 Counter를 반환한다.
    answer = collections.Counter(participant) - collections.Counter(completion)

    # 4. counter의  key값을 반환한다.
    return list(answer.keys())[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))


