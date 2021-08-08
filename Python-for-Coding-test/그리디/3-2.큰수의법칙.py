n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())), reverse = True)
first = data[0]
second = data[1]
sum = (first * k + second) * (m // (k + 1)) + first * (m % (k + 1))

print(sum)

# 파이썬에서 여러 데이터를 한 번에 입력받을 때는 map(int, input().split())


