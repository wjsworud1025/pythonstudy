# reverse()나 슬라이싱을 사용하지 않고 반복문으로 반대로 리스트 출력
numbers = [1, 2, 3, 4, 5]

i = len(numbers)-1                  #최초 len()함수를 사용해 넘버스의 마지막 값의 번호를 선언
re_numbers = []                     #반대로 출력된 list를 저장하는 빈 index를 생성
while i >= 0:                       #선언한 i(index)의 값이 0보다 커지거나 같을때 까지 반복계산(0=넘버스의 첫 숫자)
    re_numbers.append(numbers[i])   #선언한 넘버스의 인덱스 번호 숫자를 빈 인덱스에 저장
    i-= 1                           #선언한 마지막 인덱스 번호에서 1씩 차감하여 올림
print(re_numbers)                   #최종 출력된 리스트를 출력
