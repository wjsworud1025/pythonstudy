#가변 매개변수
# def 함수_이름(매개변수, 매개변수, ..., *가변_매개변수):    문장

#- 가변 매개변수 뒤에는 일반 매개변수가 올 수 없습니다.
#- 가변 매개변수는 하나만 사용할 수 있습니다.

def print_n_times(n, *values):               # 가변 매개변수 *values는 리스트처럼 사용
    for i in range(n):
                    for value in values:     # values는 리스트처럼 활용합니다.
                                print(value)
print()                                      # 단순한 줄바꿈
# 함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")