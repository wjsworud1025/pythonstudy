"""사용자 정의 모듈을 불러와 사용하는 실행 예제.

실행 방법:
    python module/main_module.py

이 파일과 ``math_module.py``가 같은 폴더에 있으므로 모듈 이름만 사용해
import할 수 있다. 확장자인 ``.py``는 import 문에 적지 않는다.
"""


# 방법 1: 모듈 전체를 가져온다.
#
# 사용할 때 ``모듈이름.함수이름()`` 형태로 작성하기 때문에 함수가 어느
# 모듈에서 왔는지 한눈에 알 수 있다. 일반적으로 이해하기 쉬운 방식이다.
import math_module


# 방법 2: 모듈에서 필요한 항목만 가져온다.
#
# 가져온 함수는 모듈 이름 없이 ``multiply()``처럼 바로 호출할 수 있다.
# 이름이 같은 함수가 현재 파일에 있으면 충돌할 수 있으므로 주의한다.
from math_module import multiply


# 방법 3: 가져오는 항목에 별칭(alias)을 붙인다.
#
# 함수 이름이 길거나, 현재 파일의 다른 이름과 구별하고 싶을 때 사용한다.
from math_module import divide as safe_divide


def main():
    """모듈의 변수와 함수를 여러 방식으로 사용한다."""
    first_number = 30
    second_number = 7

    print(f"사용 중인 모듈: {math_module.MODULE_NAME}")
    print(f"계산할 값: {first_number}, {second_number}\n")

    # 모듈 전체를 import했으므로 ``math_module.``을 앞에 붙인다.
    result_add = math_module.add(first_number, second_number)
    result_subtract = math_module.subtract(first_number, second_number)

    # from ... import로 가져온 함수는 함수 이름만으로 호출한다.
    result_multiply = multiply(first_number, second_number)

    # 별칭을 지정한 함수는 원래 이름이 아니라 별칭으로 호출한다.
    result_divide = safe_divide(first_number, second_number)

    print("개별 함수 호출 결과")
    print("덧셈:", result_add)
    print("뺄셈:", result_subtract)
    print("곱셈:", result_multiply)
    print("나눗셈:", result_divide)

    print("\n여러 결과를 한 번에 반환하는 함수")
    results = math_module.calculate_all(first_number, second_number)
    for operation, value in results.items():
        print(f"{operation}: {value}")

    # 나눗셈 함수에서 발생시킨 ValueError를 호출하는 파일에서 처리한다.
    # try 블록에서 오류가 발생하면 프로그램이 즉시 종료되는 대신,
    # 일치하는 except 블록으로 이동한다.
    print("\n예외 처리 예제")
    try:
        math_module.divide(first_number, 0)
    except ValueError as error:
        print("계산 실패:", error)


# 이 조건을 사용하면 main_module.py를 직접 실행할 때만 main()이 호출된다.
# 나중에 다른 파일에서 main_module을 import해도 예제 출력이 자동 실행되지
# 않으므로, 실행 코드와 재사용 가능한 코드를 안전하게 분리할 수 있다.
if __name__ == "__main__":
    main()
