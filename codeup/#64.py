#64 if else 구문으로 정수 3개 가장 작은 값 출력
a,b,c=map(int,input().split())
print(a if a<b and a<c
   else b 
   if b<a and b<c
   else c)
