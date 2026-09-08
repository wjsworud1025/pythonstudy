#함수를 받아 함수를 실행
def call_10_times(func):    #callback 함수
    for i in range(10):
        func()  #callback 함수

def print_hello():
    print("yaaaa!!")

call_10_times(print_hello)

# filter(함수, 리스트) - 리스트요소를 함수에 넣고 리턴값이 True 면 호출
# map(함수, 리스트) - 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
#함수를 매개변수로 사용하는 대표적인 표준 함수
