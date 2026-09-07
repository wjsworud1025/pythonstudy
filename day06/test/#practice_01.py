#학생 성적 관리 시스템 — [딕셔너리 + 리스트 + 함수 + 반복문]
#1. 학생을 추가하는 함수 `add_student(name, score)`
#2. 전체 평균을 구하는 함수 `get_average()`
#3. 평균 이상인 학생만 출력하는 함수 `get_top_students()`
def get_input(prompt, value):
    try:
        return input(prompt)
    except EOFError:
        print(f"입력처리 불가 -> {value} 기본 값으로 진행합니다.")
        return value

students = [{"이름": "김클라라", "점수": 90},
            {"이름": "이개발", "점수": 75},
            {"이름": "장혁수", "점수": 68},
            {"이름": "유지나", "점수": 39},
            {"이름": "강힘찬", "점수": 93}]


def add_student(name, score):
    students.append({"이름":name,"점수":score})
    print(students)

def get_average():
    total=0
    for student in students:
        total+=student["점수"]
    if not students:
        return 0
    return total/len(student)
        # for key, value in student.items():
        #     if isinstance(student[key], int):
        #         value_list.append(value)
        #         total=0
        #         for aver in value_list:
        #             total=0+aver
        #         average=total/len(value_list)
    #return average

def get_top_students():
    top_students = []
    for student in students:
        avr=get_average()
        if student["점수"]>=avr:
            top_students.append(student)
    return(top_students)