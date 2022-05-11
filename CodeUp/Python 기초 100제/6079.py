# 정수를 하나 입력받는다.
# 1부터 입력받은 정수까지 차례대로 더한다.
# 더하는 와중에 연산의 합이 입력받은 정수와 같거나 더 커졌을 때,
# 연산을 멈추고 마지막에 더한 정수를 출력한다.

# a = int(input())
# b = int(0)
# c = 0
# for i in range(1, a+1):
#      b =+ i
#      c = c+b
#      if c >= a:
#           print(b)
#           quit()


# 모범답안
n = int(input())
s = 0
t = 0
while s < n:
     t = t+1
     s = s+t

print(t)