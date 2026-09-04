#두 딕셔너리 병합하기
#menu1을 기준으로 menu2의 내용을 합쳐
#겹치는 키 "라떼"는 menu2의 값으로 덮어써서
#하나의 딕셔너리로 만들고, 그 결과를 items()로 반복하며
#"메뉴명: 가격" 형태로 한 줄씩 출력하세요.

menu1 = {"커피": 4000, "라떼": 4500}
menu2 = {"라떼": 5000, "쿠키": 3000}

menu1.update(menu2)
for menu, price in menu1.items():
	print(f"{menu}: {price}")

# merged() 활용하기
merged = menu1.copy()
merged.update(menu2)
for menu, price in merged.items():
    print(f"리뉴얼된 메뉴 {menu}: {price}")

merged2 = {k:v for d in (menu1, menu2) for k,v in d.items()}
print(merged2)