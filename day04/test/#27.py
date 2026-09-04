# range 3개 매개변수로 1부터 100 사이의 짝수 합
# range(A, B, C) 형태만 사용해서(if문 없이)

result=0
for i in range(2,100,2):
    result+=i
print(result)