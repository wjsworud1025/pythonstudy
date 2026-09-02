#90 기초 종합 수 나열 3(수열)
a,m,d,n=map(int, input().split())
result = a
for i in range(n - 1):
    result*=m
    result+=d
print(result)
