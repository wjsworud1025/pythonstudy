# 누적합이 처음으로 500을 넘는 순간의 숫자와 합
result = 0                                  #결과값을 0(초기화)로 선언
number = 1                                  #시작값을 1로 선언

while True:                        #while문을 True로 적용해 무한 루프 설정
    result += number               #결과값에 시작값을 반복해서 더함
    if result > 500:               #결과값이 500이 넘었다면,
        break                      #반복 계산을 멈춤
    number += 1                    #시작값에 1씩 계속 더하여 위로 올린다
print(f"{number},{result}")        #최종적으로 산출된 결과값을 f:{}함수로 출력
