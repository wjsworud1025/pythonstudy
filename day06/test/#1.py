#리스트로 평균 구하기 — [데이터구조 + 반복문]
#for 문 활용

scores = [85, 92, 78, 90, 88]

total=0
for i in scores:
    total+=i
everege=int(total)/len(scores)
print(everege)