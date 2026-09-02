#97 설탕과자 뽑기
w,h=map(int,input().split())
b=[]
for i in range(w):
    b.append([])
    for j in range(h):
        b[i].append(0)
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    x-=1
    y-=1
    for j in range(l):
        if d==0:
            b[x][y+j]=1
        else:
            b[x+j][y]=1
for i in range(w):
    for j in range(h):
        print(b[i][j],end=" ")
    print()
