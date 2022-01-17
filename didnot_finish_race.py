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
        answer = print('"'+ sub_participant[i]+'"')

    return answer

solution(participant, completion)