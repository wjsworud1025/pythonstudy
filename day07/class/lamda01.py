# lamda 매개변수: 리턴값
#람다(lamda): 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 번거롭고,
#            코드 낭비라 생각이 들때 함수를 간단하고 쉽게 선언하는 방법
#            () > {} 1회용 함수를 만들때 사용

power = lambda x: x*x
under_3 = lambda x: x<3

print(power(2))
print(under_3(2))

list_a=[1,2,3,4,5]
output_a = map(power, list_a)
output_b = filter(under_3, list_a)

print("lamda_output_a:", list(output_a))
print("lamda_output_b:", list(output_b))

output_c = map(lambda x : x*x, list_a)
output_d = filter(lambda x : x<3, list_a)

print("lamda_output_c:",list(output_c))
print("lamda_output_d:",list(output_d))
