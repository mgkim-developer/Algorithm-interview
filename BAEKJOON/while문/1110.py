input_num = int(input())
num = input_num # num변수에 인풋넘을 지정

count = 0
while True:
    sum_num = (num // 10) + (num % 10)
    new_num = ((num %10)*10) + (sum_num %10)
    count += 1 #사이클 횟수

    if new_num == input_num:
        break
    num = new_num
print(count)