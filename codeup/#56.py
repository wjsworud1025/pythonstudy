#56 bool() 활용 참/거짓이 서로 다를 때에만 참 출력
a,b=map(int,(input().split()))
print(bool(a)!=bool(b))
