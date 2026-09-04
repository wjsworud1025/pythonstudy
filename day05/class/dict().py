# .get - 열쇠(key)로 서랍(value)열기
student = {"name": "클라라", "course": "AI서비스개발"}
print(student["name"]) #출력: 클라라
print(student.get("age")) #출력: None0
print(student.get("age",20)) #출력: 20(없을 때 기본값 지정 가능)

# .keys() - 모든 이름표(key) 확인하기
student = {"name": "클라라", "course": "AI서비스개발"}
print(student.keys()) #출력: dict_keys['name', 'course']

# .values() - 모든 내용물(value) 확인하기
student = {"name": "클라라", "course": "AI서비스개발"}
print(student.values()) #출력: dict_values['클라라', 'AI서비스개발']

# 응용1. .items - 이름표과 내용물을 짝지어 순회하기
profile = {"이름": "클라라", "관심분야": "AI 서비스 기획"}
for key, value in profile.items():
    print(f"{key}:{value}") #출력: 이름: 클라라 \n 관심분야: AI 서비스 기획

# 응용2. .update() - 내용물 추가/수정하기
user = {"name": "클라라", "level": "초급"}
user.update({"level": "중급", "course_week": 3})
print(user) #출력: {'name': '클라라', 'level': '중급', 'course_week': 3}

# 실무1. 중첩 딕셔너리(Nested Dictionary) - 서랍 속의 또 다른 서랍장
# 딕셔너리["key1"]["key2"]

# 실무 예시: OpenAI API 응답 형태를 흉내낸 딕셔너리
api_response = {    "id": "chatcmpl-123",   
                    "choices": [ { "message": { "role": "assistant",
                    "content": "안녕하세요! 무엇을 도와드릴까요?"  } 
                     }  
                      ]
                }
answer = api_response["choices"][0]["message"]["content"]
print(answer)