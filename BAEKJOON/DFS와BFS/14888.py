n = int(input())
# print(n)
num_list = list(map(int, input().split()))
# print(num_list)
add, minus, multiple, divide = map(int, input().split())
# print(add, minus, multiple, divide)

min_result = 1e9
max_result = -1e9

def dfs(i, compare, add, minus, multiple, divide):
    global max_result, min_result
    if i == n:
        max_result = max(max_result, compare)
        min_result = min(min_result, compare)
        return
    if add != False:
        dfs(i + 1, compare + num_list[i], add - 1, minus, multiple, divide)
    if minus != False:
        dfs(i + 1, compare - num_list[i], add, minus - 1, multiple, divide)
    if multiple != False:
        dfs(i + 1, compare * num_list[i], add, minus, multiple - 1, divide)
    if divide != False:
        dfs(i + 1, int(compare / num_list[i]), add, minus, multiple, divide - 1)

dfs(1, num_list[0], add, minus, multiple, divide)
print(max_result)
print(min_result)