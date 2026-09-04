#len() - 글자수 세기
name="AI 개발자"
print(len(name)) #출력: 5  (한 글자당 1개씩 카운트)

#.upper() / .lower() - 대소문자 바꾸기
word="Hello Python"
print(word.upper()) #출력: HELLO PYTHON
print(word.lower()) #출력: hello python

#.strip() - 양쪽 공백/문자 제거
user_input="   챗봇에게 질문할게요    "
print(user_input.strip()) #출력: 챗봇에게 질문할게요
print(user_input) #출력:    챗봇에게 질문할게요    

#.spilt() - 구분자로 잘라서 리스트 만들기
stentece="사과,바나나,포도"
fruits=stentece.split(",")
print(fruits) #출력: ['사과','바나나','포도']

#.replace() - 특정 글자 바꾸기 >> 게임 채팅창 검열
review="이 서비스는 별로에요"
fixed=review.replace("별로에요","최고에요")
print(fixed) #출력: 이 서비스는 최고에요

#f-string(포맷팅) - 변수를 문자열 안에 끼워넣기
user_name="클라라"
question="파이썬 딕셔너리 사용법"
#실무 예시: 사용자 입력값을 넣어 AI에게 보낼 프롬프트를 자동 생성
prompt=f"{user_name}님이 '{question}'에 대해 질문했습니다. 초보자 눈높이로 답변해주세요"
print(prompt)
#출력: 클라라님이 '파이썬 딕셔너리 사용법'에 대해 질문했습니다. 초보자 눈높이로 답변해주세요

#