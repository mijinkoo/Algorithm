# 소스1
'''n, k = map(int, input().split())
count = 0
while (n != 1):
    count += 1
    if n % k == 0:
        n = n//k
    else:
        n -= 1

print(count)'''

# 소스2
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target # 이게... n = n % k 아닌가...?
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
