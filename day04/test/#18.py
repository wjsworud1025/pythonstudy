# 리스트 최댓값/최솟값 동시에 찾기
numbers = [45, 12, 89, 3, 67, 21]

largest = numbers[0]                            #최댓값을 넘버스의 index 0번으로 임의의 값 선언
smallest = numbers[0]                           #최솟값을 넘버스의 index 0번으로 임의의 값 선언
for number in numbers:                          #넘버스 list의 index에서 data를 하나씩 넘버로 호출
    if largest < number:                        #호출한 숫자가 임의의 값이 설정된 최댓값보다 크면,
        largest = number                        #임의의 값을 호출한 숫자로 변경
    if smallest > number:                       #호출한 숫자가 임의의 값이 설정된 최솟값보다 작으면,
        smallest = number                       #임의의 값을 호출한 숫자로 변경
print(f"{largest}/{smallest}")                  #f"{}"를 활용하여 최댓값과 최솟값을 함께 출력
