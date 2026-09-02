#79 while 조건식으로 반복문 실행
n=int(input())
s=0
while True:
    s+=1
    n-=s
    if n<=0:
        print(s)
        break
