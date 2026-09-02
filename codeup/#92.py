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
