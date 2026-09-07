#온라인 쇼핑몰 장바구니 계산기 — [리스트/딕셔너리 + 함수 + 제어문]
#1. 총 금액을 계산하는 함수 `calculate_total(cart)`
#2. 총 금액이 **50,000원 이상이면 10% 할인**을 적용하는 조건문 추가
#3. 최종 결제 금액 출력

cart = [{"상품명": "키보드", "가격": 50000, "수량": 1},
        {"상품명": "마우스", "가격": 20000, "수량": 2}
        ]

def calculate_total(cart):
    total = 0
    for goods in cart:
        total += goods["가격"] * goods["수량"]
    return total

def apply_discount(total):
    if total >= 50000:
        discount = total // 10
        return total - discount
    return total

print("cart 실행")
subtotal=calculate_total(cart)
discount_total=apply_discount(subtotal)

print(f"할인 전 금액: {subtotal}원\n최종 결제 금액: {discount_total}원")
