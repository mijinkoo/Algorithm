def solution1(price, money, count):
    return max(0, price*count*(count+1)/2-money)

def solution2(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += price*i
    return max(0, sum-money)