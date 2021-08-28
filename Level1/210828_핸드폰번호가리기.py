# 소스1.
def solution(phone_number):
    number = list(phone_number)
    for i in range(len(number) - 4):
        number[i] = '*'
    return ''.join(number)

# 소스2. 
# 간결한 버전
def solution2(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]

phone_number = "027778888"
print(solution(phone_number))