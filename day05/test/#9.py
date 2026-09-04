#문장에서 단어 개수와 가장 긴 단어 찾기
#문장이 총 몇 개의 단어로 이루어져 있는지
#가장 긴 단어가 무엇인지 각각 출력

sentence = "Python is a powerful and easy programming language"
keyword=sentence.split(' ')

longest=keyword[0]
for i in keyword:
    if len(longest)<=len(i):
        longest=i
print(f"{len(keyword)} / {longest}")

#max 함수 사용하기
print(f"{max(keyword)} / {len(keyword)}")

#리스트 컴프리헨션(List Comprehension) 활용하기
lengths=[len(w) for w in keyword]
longest2= keyword[lengths.index(max(lengths))]
print(len(keyword),longest2)