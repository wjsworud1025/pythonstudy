#딕셔너리로 정보 조회하기 — [데이터구조]
# 키(key)를 이용해 "이름"과 "전공"만 출력

student = {"이름": "김클라라", "나이": 25, "전공": "컴퓨터공학"}
key = student.keys()
result = []
for item in key:
	if not isinstance(student[item], int):
		result.append(item)
print(result)
