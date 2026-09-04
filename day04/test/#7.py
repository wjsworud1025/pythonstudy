# 리스트에서 짝수 개수 세기
numbers = [3, 8, 15, 22, 7, 40, 11]

counter = 0                 #카운팅된 숫자의 수 0(초기화)로 선언
for number in numbers:      #넘버스에서 변수로 data를 하나씩 호출
    if number % 2 == 0:     #호출된 숫자를 2로 나누어 0이 되는지, 짝수 검증
        counter += 1        #짝수로 판별되면 앞서 선언한 숫자에 1을 더함
print(counter)              #최종적으로 카운팅된 짝수를 출력
