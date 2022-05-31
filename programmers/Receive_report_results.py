'''
- 신고 횟수에 제한은 없다.
- 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고횟수는 1회로 처리
- k번 이상 신고된 유저는 게시판 이용 정지
- 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
- 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용정지를 시키면서 정지메일 발송

예시에서는 2번(K번)이상 신고당한 사람은 게시판 이용 정
정지 처분

각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수 작성

-------------

report에서 각 요소당 split으로 나눠진 두번째 요소는 신고받은 유저임.
id_list의 길이로 0으로 초기화시킨 리스트를 생성한다(id_list_reported)
report에서 나온 유저는 id_list_reported 에 +1
만약, k번 이상 나왔으면 해당 요소의 값을 정지리스트[] 에 추가해서 모아놓는다.
해당 정지리스트에 있는 요소를 신고한 사람에게 메일을 보낼 것인데,
id_list의 길이로 0으로 초기화시킨 리스트를 생성한다(id_list_mail)
id_list에 있는 유저 순서대로 메일 받은 횟수를 기록해서 반환한다.
'''


def solution(id_list, reports, k):
    dic_report = {id: [] for id in id_list}  # 해당 key를 신고한 사람이 value인 딕셔너리
    answer = [0] * len(id_list)  # 메일 받을 횟수 담을 리스트 (제출할 정답요소)
    reports = list(set(reports))  # 동일인이 특정인 중복 신고 방지로 set타입 이용
    stop_id = []    # k번 이상 신고 당해서 정지당한 id 저장할 리스트

    for report in reports:  # 신고건수를 루프를 돌면서
        report = report.split(' ')  #해당 신고건수를 공백을 기준으로 split함. 즉,  report[0]은 key(신고받은id), report[1]은 value(신고한id)
        dic_report[report[1]].append(report[0]) #dic_report에다가 key가 report[1]인 것의 value에 report[0]을 저장 --> 이게 핵심 아이디어임.

    #dic_report의 keys를 리스트 타입으로 변환
    dic_report_keys = list(dic_report.keys())

    for dic_report_key in dic_report_keys:  # dic_report_keys를 루프를 돌면서,
        if len(dic_report[dic_report_key]) >= k:    #만약 dic_report에서 key가 dir_report_key 인것의 value에 저장된 요소의 개수가(신고받은횟수가) k개 이상이면,
            stop_id.append(dic_report_key)  # dic_report_key (id)는 정지 시킴 -> stop_id 에 해당 id 저장
        else:
            pass

    for s in stop_id:   # 정지된 아이디를 루프를 도는데,
        for i in dic_report[s]: #dic_report에서 정지된 아이디 (key)를 신고한 value를 루프를 돌면서,
            answer[dic_report_keys.index(i)] = answer[dic_report_keys.index(i)] + 1   # 정지당한 id를 신고했던 value를 문제에서 주어진 dic_report_keys 인덱스에 알맞게 + 1 해줌 (해당 value가 신고대상정지확인 메일받은 횟수)

    return answer





# ----------------------추가 풀이-------------------------------
def solution(id_list, report, k):
    answer = [0] * len(id_list)  # 메일 받은 횟수 저장할 list
    reports = {x: 0 for x in id_list}  # 해당 id가 신고받은 횟수 저장할 dic

    for r in set(report):
        reports[r.split(' ')[1]] = reports[r.split(' ')[1]] + 1  # 신고받은 대상을 key로 reports에서 value에  + 1

    for r in set(report):
        if reports[r.split(' ')[1]] >= k:  # r.split(' ')[1] 이  신고받은 횟수가 k번 이상이면 신고자에게 정지메일을 보낼건데,
            answer[id_list.index(r.split(' ')[0])] = answer[id_list.index(r.split(' ')[0])] + 1  # 해당 건의 id를 신고한 신고자에게 메일 +1

    return answer