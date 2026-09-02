#각각의 data(list)를 element 라고 명명함
data0=[1,2,3,4,5]
data1=["안","녕","하","세","요"]
data2=[245,"문자열",124,6360000]
#변수 data 첫번째 요소의 값을 list1 변수에 저장
list1=data0[0]
#list1에 저장된 값을 출력하고 숫자라면 +2를 수행
print(list1)
list1 = list1 +2
print(list1)
data=[1,2,3,4,5,6,7,8,9,10]
#data 리스트의 3번째 요소와 5번째 요소의 값을 합하여 list2 변수에 저장
list2=data[2]+data[4]
print('{}+{}={}'.format(data[2],data[4],list2))

list3=data[1:3]
print(data[1],data[2])
print(data[-3])
print(data2[1][0:])

#리스트 안에 리스트를 넣을 수 있다
data3=[[1,2,3],[4,5,6],[7,8,9]]
list_1=data3[0][2]
print(list_1)
list_2=data3[2][1]-data3[1][1]
print(list_2)

#예제 1
Ph_data=[['P','H','K'],['O','Y','J'],['T','N','Q']]
Python_pyt=Ph_data[0][0]+Ph_data[1][1]+Ph_data[2][0]
Python_hon=Ph_data[0][1]+Ph_data[1][0]+Ph_data[2][1]
print(Python_pyt+Python_hon)

#리스트에 요소 추가하기: append(), insert()
list_a=[1,2,3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)

print("# 리스트 중간에 요소 추가하기")
list_a.insert(3, 10) #앞의 값에서 위치를 선언하고 뒤의 값을 추가
print(list_a)

print("# 여러 요소를 한 번에 추가하기")
list_b = [1, 2, 3]
list_b.extend([10, 20, 30])
print(list_b)

list_c = [1, 2, 3]
list_d = [4, 5, 6]
# 리스트 연결 연산자로 연결하기
print(list_c + list_d)
print(list_c)   
# list_a에는 어떠한 변화도 없습니다 (비파괴적 처리)
print(list_d)   
# list_b에도 어떠한 변화도 없습니다 (비파괴적 처리)

list_c.extend(list_d)
print(list_c)


list_f=[0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")
# 제거 방법 [1] - del 키워드
del list_f[1]
print("del list_f[1]:", list_f)

# 제거 방법 [2] - pop() #리스트명.pop(인덱스)
list_f.pop(2)
print("pop(2):", list_f)

# 리스트 슬라이싱
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::-1])

# 값으로 제거 - remove()
list_r = [1, 2, 1, 2]
list_r.remove(2)
print(list_r)

# 모두 제거하기 - clear()
list_cl = [0, 1, 2, 3, 4, 5]
list_cl.clear()
print(list_cl)

#리스트 정렬하기 - sort()
list_sr = [52, 273, 103, 32, 275, 1, 7]
list_sr.sort()               
# 오름차순 정렬
print(list_sr)
list_sr.sort(reverse=True)   
# 내림차순 정렬 (키워드 매개변수 활용)
print(list_sr)