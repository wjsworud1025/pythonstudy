# while로 팩토리얼 계산
# 5! = 5 * 4 * 3 * 2 * 1을 while 반복문으로 계산
n = 5
result = 1
while n > 0:
    result *= n
    n -= 1
print(result)