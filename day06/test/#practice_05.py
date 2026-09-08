#간단한 To-Do 리스트 관리 프로그램 — [종합: 함수 + while + 데이터구조 + 제어문]
#1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리

tasks = []   # {"할일":str,"완료":bool}

def add_task(task):
    tasks.append({"할일": task, "완료": False})
    print(f"'{task}' 추가 완료")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"'{removed['할일']}' 삭제완료")
    else:
        print("잘못된 번호입니다.")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['완료'] = True
        print(f"'{tasks[index]['할일']}' 완료 처리")
    else:
        print("잘못된 번호입니다.")

def show_tasks():
    if not tasks:
        print("할일 목록이 비어 있습니다.")
        return
    for i, task in enumerate(tasks):
        status = "완료" if task["완료"] else "미완료"
        print(f"{i}. {task['할일']} [{status}]")

while True:
    menu = input("1. 추가 2. 삭제 3. 조회 4. 완료 5. 종료\n선택: ")
    if menu == "1":
        task = input("할 일을 입력하세요: ")
        add_task(task)
    elif menu == "2":
        index = int(input("삭제할 번호를 입력하세요: "))
        delete_task(index)
    elif menu == "3":
        show_tasks()
    elif menu == "4":
        index = int(input("완료할 번호를 입력하세요: "))
        complete_task(index)
    elif menu == "5":
        print("프로그램 종료")
        break
    else:
        print("잘못된 번호입니다.")