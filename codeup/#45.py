#45 연산부호+format() 활용 정수 2개 입력받아 자동 계산
f1,f2,f3=input().split()
a=int(f1)+int(f2)+int(f3)
b=format(a/3,".2f")
print(a,b)
