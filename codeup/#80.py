#80 두 개의 주사위 던지기 경우의 수 계산
n, m=(input().split())
n=int(n)
m=int(m)
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)
