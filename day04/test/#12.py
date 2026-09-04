# 1부터 30까지 FizzBuzz 출력
numbers = list(range(1, 31))                    #1부터 30의 숫자를 넘버스에 index 생성
for number in numbers:                          #생성한 넘버스 index에서 data를 하나씩 넘버로 호출
    if number % 3 == 0 and number % 5 == 0:     #호출한 data가 3과 5로 나누었을때 0이 나오면 
        print("FizzBuzz")                       #피즈버즈 출력
    elif number % 3 == 0:                       #또한 3으로 나누었을떄 0이 나오면
        print("Fizz")                           #피즈 출력
    elif number % 5 == 0:                       #또한 5로 나누었을때 0이 나오면
        print("Buzz")                           #버즈 출력
    else:                                       #모두 아니면
        print(number)                           #넘버 출력
