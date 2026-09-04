#딕셔너리에서 값 꺼내고 키 목록 확인하기
#"age" 키에 해당하는 값을 get()으로 꺼내 출력하고, info가 가진 모든 키의 목록을 출력
info = {"name": "김민수", "age": 25, "job": "학생"}

print(f"{info.get("age")} | {info.keys()}")