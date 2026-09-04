# 리스트 수 평균
numbers = [12, 25, 7, 33, 18]

result = 0                      #0인 결과값을 선언
counter = len(numbers)          #평균을 위해 나누는 수(전체 더해진 개수) 선언
for number in numbers:          #index(list)에서 data를 하나씩 호출
    result += number            #결과값(더해진 숫자)에 data를 계속 더함
print(result / counter )        #결과값을 리스트의 길이만큼 나누기
