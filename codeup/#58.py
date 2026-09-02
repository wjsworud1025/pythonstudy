#58 boll() 활용 둘 다 거짓일 경우만 참 출력하기
a,b=map(int,(input().split()))
print(not(bool(a) or bool(b)))
