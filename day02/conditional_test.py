#끝자리로 짝수와 홀수 구분

# 1.%연산자 활용
n=(input("정수를 입력>"))
last_char=n[-1] #index는 문자로 받는다, 정수로 받을 수 없다.
last_char=int(last_char)
if last_char%2==0:
    print(f"{n}은 짝수입니다.")
else:
    print(f"{n}은 홀수입니다.")

# 2. in연산자 활용
n=(input("정수를 입력>"))
last_char=n[-1]
if last_char in "02468":
    print(f"{n}은 짝수입니다.")
else:
    print(f"{n}은 홀수입니다.")

#3 끝자리로 짝수와 홀수 구분
n=(input("정수를 입력>"))
last_char=n[-1]
last_char=int(last_char)

if last_char == 0 or last_char == 2 or last_char == 4 or last_char == 6 or last_char == 8:
    print(f"{n}은 짝수입니다.")
else:
    print(f"{n}은 홀수입니다.")