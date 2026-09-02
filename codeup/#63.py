#63 if else 구문으로 정수 2개 입력받아 더 큰 값 출력
a,b=map(int,input().split())
c=(a if (a>=b)
   else b)
print(c)
