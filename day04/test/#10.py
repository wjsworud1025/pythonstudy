# 1부터 100까지의 합 구하기 (while)
number = 1              #시작 숫자 선언
result = 0              #최종 합의 값을 0(초기화)으로 선언
while number <= 100:    #while의 종료 조건으로 선언한 숫자가 종료 숫자인 100이하가 되면 종료
    result += number    #선언한 최종합에 호출한 값을 더하기
    number += 1         #더하는 값을 1씩 증가
print(result)           #최종 출력

