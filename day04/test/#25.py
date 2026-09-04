# 1부터 50까지의 숫자 중 3의 배수를 제외한 수의 합
result = 0
for number in range(1, 51):
    if number % 3 == 0:
        continue
    result += number
print(result)