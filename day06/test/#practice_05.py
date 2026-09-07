#간단한 To-Do 리스트 관리 프로그램 — [종합: 함수 + while + 데이터구조 + 제어문]
#1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리

tasks = []

def add_task():
	task = input("할 일을 입력하세요: ")
	tasks.append({"할일": task, "완료": False})

def delete_task():
	show_tasks()
	number = int(input("삭제할 번호를 입력하세요: "))
	tasks.pop(number - 1)

def show_tasks():
	number = 1
	for task in tasks:
		print(number, task)
		number += 1

while True:
	menu = input("1. 추가 2. 삭제 3. 조회 4. 종료: ")
	if menu == "1":
		add_task()
	elif menu == "2":
		delete_task()
	elif menu == "3":
		show_tasks()
	elif menu == "4":
		break