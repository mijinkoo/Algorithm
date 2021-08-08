# 소스1
'''
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
min_list = []
for i in range(n):
    min_list.append(min(data[i]))
answer = max(min_list)

print(answer)
'''

# 소스2
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)