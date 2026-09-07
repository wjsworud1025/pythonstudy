#구구단 출력하기 — [반복문(while) + 제어문]
#while문을 사용해 사용자가 입력한 숫자(2~9)의 구구단을 출력

n = 2
while n < 10:
    m = 1
    while m < 10:
        print(n, "X", m, "=", n * m)
        m += 1
    n += 1