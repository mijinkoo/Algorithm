# 소스1.
# 두 숫자 입력 받기
# -> map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)

# 소스2.
# for 문 사용하지 않는 방법
answer = ('*' * a + '\n') * b
print(answer)