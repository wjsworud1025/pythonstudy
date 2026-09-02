#94 이상한 출석 부르기 3
n=int(input())
numbers=list(map(int,input().split()))
smallest=numbers[0]
for i in range(1,n):
    if numbers[i]<smallest:
        smallest=numbers[i]
print(smallest)
