n = int(input())
# print(n)
house = list(map(int, input().split()))
house.sort()

print(house[(n-1)//2])