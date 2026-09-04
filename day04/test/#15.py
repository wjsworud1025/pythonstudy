# 리스트 중복값 제거
numbers = [1, 3, 2, 3, 5, 1, 4, 2]

unique_numbers = []                         #중복되지 않는 전체 list를 빈 index로 생성
for number in numbers:                      #넘버스 index에서 data를 하나씩 넘버로 호출
    if number not in unique_numbers:        #호출한 data가 만들어둔 빈 index에 없으면,
        unique_numbers.append(number)       #생성한 data에 추가
print(unique_numbers)                       #최종 완성된 중복되지 않는 전체 list 출력
