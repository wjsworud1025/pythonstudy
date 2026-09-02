#77 for range() + 조건 함수로 반복문 실행
n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print(s)
