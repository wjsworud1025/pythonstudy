#텍스트 단어 빈도수 분석기 — [딕셔너리 + 반복문 + 함수]
#1. 공백 기준으로 단어를 나누고(`split()`), 딕셔너리에 `{단어: 등장횟수}` 형태로 저장
#2. 가장 많이 등장한 단어 TOP 3을 출력


# def restore_word(word):
#     particles = ["으로", "에게", "에서", "까지", "부터", "처럼", "보다", "만큼", "이랑", "랑", "은", "는", "이", "가", "을", "를", "도", "만", "로"]
#     for particle in particles:
#         if word.endswith(particle) and len(word) > len(particle):
#             return word[:-len(particle)]
#     return word

# keyword = []
# for data in text.split():
#     keyword.append(restore_word(data))
# count = []
# for data in keyword:
#     count.append(keyword.count(data))
# prequncy = {}
# index = 0
# for data in keyword:
#     if data not in prequncy:
#         prequncy[data] = count[index]
#     index += 1

# items = list(prequncy.items())
# for i in range(len(items) - 1):
#     for j in range(len(items) - 1 - i):
#         if items[j][1] < items[j + 1][1]:
#             items[j], items[j + 1] = items[j + 1], items[j]

# prequncy = dict(items)
# print(f"{items[0][0]} : {items[0][1]} / {items[1][0]} : {items[1][1]} / {items[2][0]} : {items[2][1]}")

def count_word(sentence):
    words = sentence.split()#split()->공백을 기준으로 문자열을 리스트로 반환
    counts = {}
    for word in words:
        #dict.get(key,기본값) : key 가 존재한다면 해당 값을 리턴, 없으면 기본값 0 리턴
        counts[word] = counts.get(word, 0) + 1
    return counts

text ="이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"

word_count = count_word(text)

#2 내림차순 정렬 : 가장 많이 등장하는 단어 TOP3 
word_count = count_word(text)

items = list(word_count.items())
print(items)
for i in range(len(items) - 1):
    for j in range(len(items) - 1 - i):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

top3 = items[:3]

# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
# top3 = sorted_words[:3]

for word, count in top3:
    print(f"{word} : {count}")