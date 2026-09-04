#단어별 등장 횟수 세기 (빈도수 계산)
#text를 단어 단위로 나눈 뒤, 각 단어가 몇 번씩 등장하는지
#딕셔너리 형태로 만들어 출력하세요.

text = "apple banana apple cherry banana apple"

keyword=sorted(text.split(' '))
fr = {}
for i in range(len(keyword)):
	current=keyword[i]
	if current in fr:
		continue
	count=0
	for j in range(len(keyword)):
		if current==keyword[j]:
			count+=1
	fr[current]=count
print(fr)

