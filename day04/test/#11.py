# 구구단 2~9단 전체 출력하기 (중첩 for)
for d in range(2, 10):                      #구구단을 출력할 범위를 range(시작, 종료+1)까지 반복계산
    for m in range(1, 10):                  #곱할 값을 range(시작, 종료+1)까지 다시 반복계산
        print(f"{d} X {m} = {d * m}")       #"for d~" 구문에서 d값, "for m~" 구문에서 m값을 가져와 f"{} 으로 출력

# 구구단 2~9단 전체 출력하기 (중첩 while)
dan = 2
while dan <= 9:
    multiplier = 1
    while multiplier <= 9:
        print(f"{dan} x {multiplier}={dan * multiplier}")
        multiplier += 1
    dan += 1