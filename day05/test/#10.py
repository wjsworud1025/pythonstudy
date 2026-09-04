#단어별 등장 횟수 세기 (빈도수 계산)
#text를 단어 단위로 나눈 뒤, 각 단어가 몇 번씩 등장하는지
#딕셔너리 형태로 만들어 출력하세요.

text = "apple banana apple cherry banana apple"

keyword=text.split(' ')
result = {}
for i in range(len(keyword)):
	current=keyword[i]
	if current in result:
		continue
	count=0
	for j in range(len(keyword)):
		if current==keyword[j]:
			count+=1
	result[current]=count
print(result)

#clean code
#1 count = 딕셔너리 생성 
count = {}
#2 문자열 공백을 기준으로 split() => 리스트로 생성 
words = text.split()    #단어 단위로 나눠서 리스트 생성
#3 분리된 단어별 횟수를 센다
for w in words:    #단어를 하나씩 순서대로 확인 
    if w in count:
        count[w] = count[w]+1
    else:
        count[w] = 1
#4 count 딕셔너리 출력
print(count)