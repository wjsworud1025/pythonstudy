#78 while() + 조건 함수로 반복문 실행
c=ord(input())
while True:
    print(chr(c))
    if c==ord('q'):
        break
    c=ord(input())
