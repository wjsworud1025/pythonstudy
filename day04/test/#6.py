# while 반복문으로 1부터 5까지 출력
start = 1           #시작하는 숫자인 1을 선언
while True:         #반복계산을 위해 while True 호출
    if 5 < start:   #마지막 출력 숫자인 5보다 시작하는 숫자가 크면
        break       #반복을 중단
    print(start)    #선언해둔 숫자를 출력
    start += 1      #선언한 숫자에 1을 반복해서 더한다
