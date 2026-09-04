#문장에서 단어 개수와 가장 긴 단어 찾기
#문장이 총 몇 개의 단어로 이루어져 있는지
#가장 긴 단어가 무엇인지 각각 출력

sentence = "Python is a powerful and easy programming language"
keyword=sentence.split(' ')
print(keyword)
print(len(keyword))

longest=keyword[0]
for i in keyword:
    if len(longest)<=len(i):
        longest=i
print(f"{len(keyword)} / {longest}")