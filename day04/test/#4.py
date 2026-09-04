# max() 함수를 사용하지 않고 최댓값 찾기
numbers = [12, 25, 7, 33, 18]

largest = numbers[0]            #가장 큰 수를 임의수인 넘버스의 첫 숫자로 선언
for number in numbers:          #넘버스의 data를 넘버로 하나씩 호출
    if largest < number:        #앞에서 선언한 임의의 숫자와 호출된 숫자를 비교
        largest = number        #if문에서 임의의 숫자보다 호출된 숫자가 크면 임의의 숫자 교체
print(largest)                  #최종 가장 큰 수 출력
