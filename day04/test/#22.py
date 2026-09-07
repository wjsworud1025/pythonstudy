# 소수 판별
number = 3
n = 2
prime = True
if number < 2:
    prime = False
while n < number:
    if number % n == 0:
        prime = False
        break
    n += 1
if prime:
    print("PRIME")
else:
    print("NOT PRIME")