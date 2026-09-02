#88 기초 종합 수 나열 1(등차)
a,d,n=map(int,input().split())
for i in range(a,(a+d*n)-d+1):
    if i==(a+d*n)-d:
        print(i)
