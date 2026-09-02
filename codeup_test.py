#1 print ("Hello")
print("Hello")

#2 print 개별(띄어쓰기 포함) 출력
print("Hello", "World")

#3 print 줄바꿈 출력
print("Hello\nWorld")

#4 print''구문 출력
print("'Hello'")

#5 print "" 구문 출력
print('"Hello World"')

#6 print 특수문자 출력
print('\"!@#$%^&*()\'')

#7 print 특수문자+문자 출력
print("\"C:\\Download\\'hello'.py\"")

#8 print 특수문자+문자 출력
print('print("Hello\\nWorld")')

#9 input 문자 출력
c = input()
print(c)

#10 input 정수(int()) 출력
n = input()
n = int(n)
print(n)

#11 input 소수(float()) 출력
f = input()
f = float(f)
print(f)

#12 input 2개 이상의 정수 출력 (두개 이상의 값을 받았을 때 split으로 값을 나누는 기준을 저장한다.)
a, b=input().split()
a=int(a)
b=int(b)
print(a)
print(b)

#13 input 2개 이상의 문자 출력
a, b=input().split()
print(a)
print(b)

#14 input 실수 1개 3번 출력하기
f=float(input())
print(f)
print(f)
print(f)

#15 input 정수 2개를 입력받아 그대로 출력
a, b=input().split()
a=int(a)
b=int(b)
print(a)
print(b)

#16 input 문자 2개를 입력받아 순서바꿔 출력
a, b=input().split()
print(b, a)

#17 input 문장 1개를 입력받아 3번 출력
text = input()
print(text, text, text)

#18 input+sep 시간 입력받아 그대로 출력하기(sep가 공백을 없애고 :로 출력)
a, b = input().split(':')
print(a, b, sep=':')

#19 input+sep 연월일 입력받아 순서 바꿔 출력하기(sep가 공백을 없애고 -로 출력)
y, m, d = input().split('.')
print(d, m, y, sep='-')

#20 input+sep 주민번호 입력받아 순서 바꿔 출력하기(sep가 공백을 없애고 -로 출력)
a, b = input().split("-")
print(a, b, sep="")

#21 index[]활용 단어 1개 입력받아 나누어 출력
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#22 index[]활용 연월일 입력받아 나누어 출력하기
d=input()
print(d[0:2])
print(d[2:4])
print(d[4:6])

#23 index[]활용 시분초 입력받아 분만 출력
t = input().split(":")
print(t[1])

#24 합연산 활용 단어 2개 입력받아 이어 붙이기
s1, s2 = input().split()
print(s1+s2)

#25 합연산 활용 정수 2개 입력받아 합 계산
n1, n2 = input().split()
n1=int(n1)
n2=int(n2)
n3=n1+n2
print(n3)

#26 합연산 활용 실수 2개 입력받아 합 계산
f1, f2 = input().split()
f1=float(f1)
f2=float(f2)
f3=f1+f2
print(f3)

#27 "%x"%n활용 10진 정수 입력받아 16진수로 출력
a=input()
n = int(a)
print("%x"%n)

#28 "%X"%n 활용 10진 정수 입력받아 16진수 대문자로 출력
a=input()
n = int(a)
print("%X"%n)

#29 "%o"%n 활용 16진 정수 입력받아 8진수로 출력
a=input()
n = int(a)
print("%o"%n)

#30 ord() 활용 영문자 1개 입력받아 10진수(아스키코드)로 출력
n = ord(input())
print(n)

#31 chr() 활용 10진수(아스키코드) 입력받아 영문자 출력
n = int(input())
print(chr(n))

#32 부호변환을 활용 정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n)

#33 chr()+부호변환 활용 문자 1개 입력받아 다음 문자 출력
n=input()
print(chr(ord(n) + 1))

#34 부호변환 활용 정수 2개 입력받아 차 계산하기
a, b = input().split()
c=int(a) - int(b)
print(c)

#35 * 활용 수 2개 입력받아 곱 계산
f1, f2 = input().split()
c=float(f1) * float(f2)
print(c)

#36 * 활용 정수와 문자를 받아 반복 출력하기
w, n = input().split()
print(w*int(n))

#37 * 활용 정수와 문자를 받아 반복 출력하기
n, s = input().split()
print(int(n)*s)

#38 ** 활용 정수 2개 입력받아 거듭제곱 계산
a,b=input().split()
c=int(a)**int(b)
print(c)

#39 ** 활용 실수 2개 입력받아 거듭제곱 계산
f1, f2 = input().split()
c=float(f1)**float(f2)
print(c)

#40 // 활용 정수 2개 입력받아 나눈 몫 계산
a,b=input().split()
c=int(a)//int(b)
print(c)

#41 % 활용 정수 2개 입력받아 나눈 나머지 계산
a,b=input().split()
c=int(a)%int(b)
print(c)

#42 fomat() 활용 실수 1개 입력받아 소숫점이하 자리 변환
a=input()
a=float(a)
print( format(a, ".2f") )

#43 format() 활용 실수 2개 입력받아 나눈 결과 계산
f1,f2=input().split()
c=float(f1)/float(f2)
print(format(c, ".3f"))

#44 연산부호+format() 활용 정수 2개 입력받아 자동 계산
a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b,2))

#45 연산부호+format() 활용 정수 2개 입력받아 자동 계산
f1,f2,f3=input().split()
a=int(f1)+int(f2)+int(f3)
b=format(a/3,".2f")
print(a,b)

#46 비트시프트연산 활용 정수 1개 입력받아 2배 곱해 출력
n=int(input())
print(n<<1)

#47 비트시프트연산 활용 2의 거듭제곱 배로 곱해 출력
a,b=input().split()
a=int(a)
b=int(b)
print(a<<b)

#48 비교연산자 활용 정수 2개 입력받아 비교(크다, 작다)
a,b=map(int, input().split())
print(a<b)

#49 비교연산자 활용 정수 2개 입력받아 비교(같다)
a,b=map(int, input().split())
print(a==b)

#50 비교연산자 활용 정수 2개 입력받아 비교(크거나, 작거나 같다)
a,b=map(int, input().split())
print(a<=b)

#51 비교연산자 활용 정수 2개 입력받아 비교(다르다)
a,b=map(int, input().split())
print(a!=b)

#52 bool()활용 정수 입력받아 참 거짓 평가
a=int(input())
print(bool(a))

#53 bool()+논리연산자 활용 참 거짓 바꾸기
a = int(input())
print(not bool(a))

#54 bool() 활용 둘 다 참일 경우만 참 출력
a,b=map(int,(input().split()))
print(bool(a) and bool(b))

#55 bool() 활용 하나라도 참이면 참 출력
a,b=map(int,(input().split()))
print(bool(a) or bool(b))

#56 bool() 활용 참/거짓이 서로 다를 때에만 참 출력
a,b=map(int,(input().split()))
print(bool(a)!=bool(b))

#57 bool() 활용 참/거짓이 서로 같을 때에만 참 출력
a,b=map(int,(input().split()))
print(bool(a)==bool(b))

#58 boll() 활용 둘 다 거짓일 경우만 참 출력하기
a,b=map(int,(input().split()))
print(not(bool(a) or bool(b)))

#59 ~비트단위논리연산 비트단위로 NOT 하여 출력
a=int(input())
print(~a)

#60 &비트단위논리연산 비트단위로 AND 하여 출력
a, b = map(int, input().split())
print(a & b)

#61 |비트단위논리연산 비트단위로 OR 하여 출력
a, b = map(int, input().split())
print(a|b)

#62 ^비트단위논리연산 비트단위로 XOR 하여 출력
a, b = map(int, input().split())
print(a^b)

#63 if else 구문으로 정수 2개 입력받아 더 큰 값 출력
a,b=map(int,input().split())
c=(a if (a>=b)
   else b)
print(c)

#64 if else 구문으로 정수 3개 가장 작은 값 출력
a,b,c=map(int,input().split())
print(a if a<b and a<c
   else b 
   if b<a and b<c
   else c)

#65 if 구문으로 정수 3개 입력받아 짝수만 출력
a,b,c=map(int,input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

#66 if eles 구문 활용 정수 3개 입력받아 짝/홀 출력
a,b,c=map(int,input().split())
if a%2==0:
    print("even")
else:
    print("odd")
if b%2==0:
    print("even")
else:
    print("odd")
if c%2==0:
    print("even")
else:
    print("odd")

#67 if eles 구문 활용 정수 1개 입력받아 분류
n=int(input())
if n<0:
  if n%2==0:
    print('A')
  else:
    print('B')
else:
  if n%2==0:
    print('C')
  else:
    print('D')
    
#68 if eilf 구문으로 조건 출력
s=int(input())
if s>=90:
    print('A')
elif s>=70:
    print('B')
elif s>=40:
    print('C')
else :
    print('D')

#69 if eilf 영문자 받아 구문으로 조건 출력
s=(input())
if s=='A':
    print('best!!!')
elif s=='B':
    print('good!!')
elif s=='C':
    print('run!')
elif s=='D':
    print('slowly~')
else:
    print('what?')

#70 if else 구문으로 조건 출력
s=int(input())
if s//3==1:
    print('spring')
else:
    if s//3==2:
        print('summer')
    else:
        if s//3==3:
            print('fall')
        else:
            print('winter')

#71 while 조건식으로 반복문 실행
while True:
    a=input()
    a=int(a)
    if a==0:
        break
    else:
        print(a)

#72 while 조건식으로 반복문 실행
n=int(input())
while n!=0:
        print(n)
        n-=1

#73 while 조건식으로 반복문 실행
n=int(input())
while n>=1:
        n-=1
        print(n)

#74 while 조건식으로 반복문 실행
n=ord(input())
s=ord('a')
while s<=n:
    print(chr(s),end=' ')
    s+=1

#75 while 조건식으로 반복문 실행
n=int(input())
s=0
while s<=n:
    print(s)
    s+=1

#76 for range() 함수로 반복문 실행
n=int(input())
for i in range(n+1):
    print(i)

#77 for range() + 조건 함수로 반복문 실행
n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print(s)

#78 while() + 조건 함수로 반복문 실행
c=ord(input())
while True:
    print(chr(c))
    if c==ord('q'):
        break
    c=ord(input())

#79 while 조건식으로 반복문 실행
n=int(input())
s=0
while True:
    s+=1
    n-=s
    if n<=0:
        print(s)
        break

#80 두 개의 주사위 던지기 경우의 수 계산
n, m=(input().split())
n=int(n)
m=int(m)
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

#81 16진수 구구단 출력
n=int(input())
for i in range(1,16):
    print('%X'%n,'*%X'%i,'=%X'%(n*i), sep="")

#82 기초 종합 3 6 9 게임
n=int(input())
for i in range(1,n+1):
    num=str(i)
    if '3' in num or '6' in num or '9' in num:
        print("X",end=' ')
    else:
        print(i,end=' ')

#83 기초 종합 빛 섞어 색 만들기
r,g,b=map(int,(input().split()))
for i in range(0,r):
    for j in range(0, g):
        for k in range(0, b):
            print(i,j,k)
print(r*g*b)

#84 기초 종합 소리 파일 저장용량 계산
h,b,c,s=map(int,(input().split()))
bit=h*b*c*s
mb=bit/8/1024/1024
print("{:.1f} MB".format(mb))

#85 기초 종합 그림 파일 저장용량 계산
w,h,b=map(int,input().split())
size=w*h
bit=size*b
mb=bit/8/1024/1024
print("{:.2f} MB".format(mb))

#86 기초 종합 거기까지! 이제 그만~
n=int(input())
a=1
t=0
while True:
    t+=a
    a+=1
    if t>=n:
        break
print(t)

#87 기초 종합 3의 배수는 통과
n=int(input())
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i,end=' ')

#88 기초 종합 수 나열 1(등차)
a,d,n=map(int,input().split())
for i in range(a,(a+d*n)-d+1):
    if i==(a+d*n)-d:
        print(i)

#89 기초 종합 수 나열 2(등비)
a, r, n = map(int, input().split())
result = a
for i in range(n - 1):
    result *= r
print(result)

#90 기초 종합 수 나열 3(수열)
a,m,d,n=map(int, input().split())
result = a
for i in range(n - 1):
    result*=m
    result+=d
print(result)

#91 기초 종합 함께 문제 푸는 날
a,b,c=map(int,input().split())
d=1
while d%a!=0 or d%b!=0 or d%c!=0:
    d+=1
print(d)

#92 이상한 출석 부르기 1
n = int(input())
a = input().split() #'a'는 index 는 문자열
for i in range(n): #range(n)의 n은 반복횟수
    a[i]=int(a[i])
d=[]
for i in range(24):
    d.append(0)
for i in range(n):
    d[a[i]]+=1
for i in range(1,24):
    print(d[i],end=' ')

#93 이상한 출석 부르기 2
n = int(input())
a= input().split()
for i in range(n - 1, -1, -1):
    print(a[i], end=' ')

#94 이상한 출석 부르기 3
n=int(input())
numbers=list(map(int,input().split()))
smallest=numbers[0]
for i in range(1,n):
    if numbers[i]<smallest:
        smallest=numbers[i]
print(smallest)

#95 바둑판 좌표 찍기
d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
n=int(input())
for i in range(n):
    x,y=input().split()
    d[int(x)][int(y)]=1
for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()

#96
d = []
for i in range(19):
    d.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(19):
        d[x][j] = 1 - d[x][j]
    for j in range(19):
        d[j][y] = 1 - d[j][y]
for i in range(19):
    print(*d[i])