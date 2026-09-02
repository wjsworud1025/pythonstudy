#93 이상한 출석 부르기 2
n = int(input())
a= input().split()
for i in range(n - 1, -1, -1):
    print(a[i], end=' ')
