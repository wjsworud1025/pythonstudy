tuple_test= 10, 20, 30, 40
print("괄호가 없는 튜플의 값과 자료형 출력")
#파이썬은 data의 나열의 기본값을 tuple로 저장, 기본적으로 ()를 사용한 것과 다르지 않음
print("tuple_test:", tuple_test)    #()로 감싸진 tuple 로 출력
print("tuple_test:", type(tuple_test))  # class로 출력

# 괄호가 없는 튜플
# tuple_test01 에 자신의 이름과 친구 2명의 이름 할당
tuple_test01 = "전재경", "김희진", "강병훈" 
print(tuple_test01)
num=1
for call in tuple_test01:
    print(f"번호 {num}: {call}")
    num+=1
