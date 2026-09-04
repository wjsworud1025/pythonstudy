#문자열 나누고 다시 합치기
#쉼표(,)를 기준으로 sentence를 나눠 리스트로 만든 뒤, 
#그 리스트를 " - "(공백-하이픈-공백)로 다시 이어 붙여 하나의 문자열로 출력

sentence = "사과,바나나,포도,딸기"
new=sentence.split(",")
print(' - '.join(new))