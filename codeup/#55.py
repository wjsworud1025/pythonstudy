#55 bool() 활용 하나라도 참이면 참 출력
a,b=map(int,(input().split()))
print(bool(a) or bool(b))
