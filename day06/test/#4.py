#사칙연산 함수 만들기 — [함수]
#숫자 두 개를 매개변수로 받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 각각 반환하는 함수 4개
# (add, subtract, multiply, divide)를 정의하고 호출

a, b = map(int, input().split())

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(f"{add(a, b)} / {subtract(a, b)} / {multiply(a, b)} / {divide(a, b)}")