#82 기초 종합 3 6 9 게임
n=int(input())
for i in range(1,n+1):
    num=str(i)
    if '3' in num or '6' in num or '9' in num:
        print("X",end=' ')
    else:
        print(i,end=' ')
