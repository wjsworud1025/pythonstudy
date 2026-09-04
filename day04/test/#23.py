# 문자열 내 특정 문자 개수 세기
sentence = "banana"
target = "a"

counter = 0
for character in sentence:
    if character == target:
        counter += 1
print(counter)
