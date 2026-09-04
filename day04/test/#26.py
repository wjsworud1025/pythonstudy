# 딕셔너리 리스트에서 최고 점수 학생 찾기
students = [  # 학생 정보를 저장할 리스트를 만든다.
    {"name": "철수", "score": 85},  # 첫 번째 학생의 이름과 점수를 저장한다.
    {"name": "영희", "score": 92},  # 두 번째 학생의 이름과 점수를 저장한다.
    {"name": "민수", "score": 78},  # 세 번째 학생의 이름과 점수를 저장한다.
]  # 학생 정보 리스트를 닫는다.

best_student = students[0]                           # 첫 번째 학생을 현재 최고 점수 학생으로 정한다.
for student in students:                             # 모든 학생을 한 명씩 확인한다.
    if student["score"] > best_student["score"]:     # 현재 학생의 점수가 더 높은지 비교한다.
        best_student = student                       # 더 높은 점수의 학생을 최고 점수 학생으로 바꾼다.
print(best_student["name"], best_student["score"])   # 최고 점수 학생의 이름과 점수를 출력한다.


best_student = students[0]                           # 두 번째 풀이에서도 첫 번째 학생을 최고 점수 학생으로 정한다.
for student in students:                             # 모든 학생을 한 명씩 확인한다.
    count = 0                                        # 딕셔너리 값의 순서를 세기 위한 변수를 초기화한다.
    for key in student:                              # 현재 학생 딕셔너리의 키를 순서대로 확인한다.
        if count == 1:                               # 두 번째 값에 도달했는지 확인한다.
            score = student[key]                     # 두 번째 값인 현재 학생의 점수를 저장한다.
        count += 1                                   # 확인한 키의 개수를 하나 늘린다.
    count = 0                                        # 최고 점수 학생의 값 순서를 세기 위해 다시 초기화한다.
    for key in best_student:                         # 현재 최고 점수 학생의 키를 순서대로 확인한다.
        if count == 1:                               # 두 번째 값에 도달했는지 확인한다.
            best_score = best_student[key]           # 두 번째 값인 최고 점수를 저장한다.
        count += 1                                   # 확인한 키의 개수를 하나 늘린다.
    if score > best_score:                           # 현재 학생의 점수가 더 높은지 비교한다.
        best_student = student                       # 더 높은 점수의 학생을 최고 점수 학생으로 바꾼다.
for key in best_student:                             # 최고 점수 학생 딕셔너리의 키를 순서대로 확인한다.
    print(best_student[key], end=" ")                # 이름과 점수를 한 줄에 출력한다.