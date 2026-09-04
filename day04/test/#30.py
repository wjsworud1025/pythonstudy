#학생 성적 데이터에서 과목별 평균 구하기
students = [{"name": "철수", "korean": 80, "math": 90, "english": 85},
            {"name": "영희", "korean": 95, "math": 100, "english": 88},
            {"name": "민수", "korean": 70, "math": 60, "english": 75},]

for student in students:
    score_keys = []
    for key, value in student.items():
        if type(value) == int:
            score_keys.append(key)
    total = 0
    for key in score_keys:
        total += student[key]
    average = total / len(score_keys)
    print(f"{student['name']}: {average}")