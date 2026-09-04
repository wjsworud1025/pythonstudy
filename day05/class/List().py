#len() - 담긴 물건 개수 세기
cart=["사과","우유","빵"]
print(len(cart)) #출력: 3

#.append() - 물건 하나 추가하기
cart=["사과", "우유"]
cart.append("빵")
print(cart)  #출력: ['사과', '우유', '빵']

# sorted()/.sort() - 순서대로 정렬하기
numbers=[5, 2, 8, 1]
print(numbers)
numbers1=sorted(numbers)
print(numbers1)
#출력:[1, 2, 5, 8](원본 numbers는 그대로)
numbers.sort()
print(numbers) #출력: [1, 2, 5, 8]  (원본 자체가 바뀜)

#'변수'.join(리스트) - 리스트 data 사이 원하는 문자를 추가
fruit=['사과', '바나나', '포도', '딸기']
print('-'.join(fruit))

# 응용1. 슬라이싱[시작:끝] - 일부만 잘라 꺼내기
menu=["김밥","라면","떡볶이","순대"]
print(menu[0:2]) #출력: ['김밥', '라면'](0번, 1번만)
print(menu[-1]) #순대(뒤에서 첫번째)

# 응용2. .index()/in - 원하는 값 찾기
skills=["Git","Python","Open AI"]
print("Python" in skills) #출력: True
print(skills.index("Python")) #출력: 1(0번부터 두번째)

# 실무1. 리스트 컴프리헨션(List Comprehension) - 반복문을 한줄로
# 실무 예시: AI API가 돌려준 답변 후보 리스트 중
# 길이가 10자 이상인 것만 필터링
ai_responses = ["네", "안녕하세요! 무엇을 도와드릴까요?",
                 "좋아요", "파이썬 학습을 시작해볼까요?"]
long_responses=[text for text in ai_responses if len(text) >= 10]
print(long_responses)
#출력: ['안녕하세요! 무엇을 도와드릴까요?', 
#           '파이썬 학습을 시작해볼까요?']

