"""사칙연산 기능을 모아 둔 사용자 정의 모듈 예제.

모듈(module)이란 Python 코드를 저장한 ``.py`` 파일을 뜻한다.
다른 파일에서 이 모듈을 import하면 아래에 정의한 변수와 함수를
새로 작성하지 않고도 재사용할 수 있다.

이 파일은 직접 실행하기보다 ``main_module.py``에서 불러와 사용하는
것을 주된 목적으로 한다.
"""


# 모듈 수준 변수도 다른 파일에서 ``math_module.MODULE_NAME``처럼
# 접근할 수 있다. 여러 함수에서 공통으로 사용할 값을 두기에 알맞다.
MODULE_NAME = "사칙연산 모듈"


def add(x, y):
    """두 수를 더한 결과를 반환한다."""
    return x + y


def subtract(x, y):
    """x에서 y를 뺀 결과를 반환한다."""
    return x - y


def multiply(x, y):
    """두 수를 곱한 결과를 반환한다."""
    return x * y


def divide(x, y):
    """x를 y로 나눈 결과를 반환한다.

    0으로 나누면 Python에서 ZeroDivisionError가 발생한다. 호출하는 쪽에서
    오류를 처리할 수도 있지만, 이 예제에서는 함수가 잘못된 입력을 즉시
    알려 주도록 명확한 메시지의 예외를 직접 발생시킨다.
    """
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y


def calculate_all(x, y):
    """두 수의 사칙연산 결과를 딕셔너리로 묶어서 반환한다.

    같은 모듈 안의 함수는 모듈 이름을 붙이지 않고 바로 호출할 수 있다.
    이 함수는 작은 함수들을 조합해 더 큰 기능을 만드는 예시다.
    """
    return {
        "덧셈": add(x, y),
        "뺄셈": subtract(x, y),
        "곱셈": multiply(x, y),
        "나눗셈": divide(x, y),
    }


# Python은 파일을 실행할 때 특수 변수 __name__을 자동으로 만든다.
#
# 1. ``python math_module.py``처럼 이 파일을 직접 실행한 경우
#    __name__의 값은 "__main__"이다.
# 2. 다른 파일에서 ``import math_module``로 불러온 경우
#    __name__의 값은 모듈 이름인 "math_module"이다.
#
# 따라서 아래 코드는 직접 실행할 때만 동작하고, import할 때는 동작하지
# 않는다. 모듈에 간단한 사용 예시나 자체 테스트를 넣을 때 자주 쓰는 구조다.
if __name__ == "__main__":
    print("math_module.py를 직접 실행했습니다.")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 × 5 =", multiply(10, 5))
    print("10 ÷ 5 =", divide(10, 5))
