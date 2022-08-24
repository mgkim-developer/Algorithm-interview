import sys
# n 입력
n = int(input())
# print(n)

# 학생 정보 입력받을 리스트
student = []
for i in range(n):
    student.append(sys.stdin.readline().split())
# print(student)

# 문제에서 주어진 조건대로 정렬
student.sort(key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for i in student:
    print(i[0])