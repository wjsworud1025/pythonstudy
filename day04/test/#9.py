# 57이라는 값이 몇 번째 인덱스에 있는지 break를 사용해 찾기
array = [273, 32, 103, 57, 52]

target = 57                             #목표로 하는 숫자 선언
counter = 0                             #카운터를 0(초기화)로 선언
while counter < len(array):             #while 반복구문 완료 조건으로 array에 배치된 data보다 카운터가 커지면 종료 설정
    if array[counter] == target:        #index에서 카운팅 만큼의 번호 데이터와 타겟값을 비교
        print(counter)                  #타겟값과 같아지면 출력
    counter += 1                        #data와 비교할때마다 카운터에 1을 더한다.

# enumerate 활용
for index, value in enumerate(array):
    if value == target:
        print(index)
        break
