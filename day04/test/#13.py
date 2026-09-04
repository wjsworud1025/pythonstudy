# 짝수만 필터링해서 새 리스트 만들기
numbers = [3, 8, 15, 22, 7, 40, 11, 6]

even = []                           #짝수를 [] 빈리스트로 index 선언
for number in numbers:              #넘버스 index에서 넘버로 호출
    if number % 2 == 0:             #호출한 숫자를 2로 나누어서 0으로 떨어지면
        even.append(number)         #짝수 빈리스트에 추가
print(even)                         #최종적으로 리스트에 추가된 짝수를 출력

# 리스트 컴프리헨션
even_list = [number for number in numbers if number % 2 == 0]
print(even_list)
