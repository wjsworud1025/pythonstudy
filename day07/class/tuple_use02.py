# a, b 에 튜플 10, 20 값 할당
a, b=10, 20
print("교환 전 값 a:", a) 
print("교환 전 값 b:", b)
a, b=b, a
print("교환 후 값 a:", a)
print("교환 후 값 b:", b)

# 리스트에서도 동일하게 쓸 수 있다.
c, d=[10, 20]
print("교환 전 값 c:", c) 
print("교환 전 값 d:", d)
c, d=d, c
print("교환 후 값 c:", c) 
print("교환 후 값 d:", d)

#튜플은 함수의 리턴에 많이 사용
#test 함수를 선언하고, test 함수는 return 값으로 10, 20 두개의 정수를 리턴
def test(input):
    if input == 0:
        True
        return 10, 20

def test2(input):
    if input == 1:
        True
        return 30, 40

def test3(input):
    if input == 2:
        True
        return 100
        
t1=int(input("test 시작"))
for fun in (test, test2, test3):
    result = fun(t1)
    if result is not None:
        print(result)

print("실무 예제 for ---- enumerate")
for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다.".format(i+1,value))


