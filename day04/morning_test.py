#1 리스트 수 합
numbers = [12, 25, 7, 33, 18]  # 여기를 채워보세요

result=0
for i in numbers:
    result+=i
print(result)

#2 리스트 수 평균
numbers = [12, 25, 7, 33, 18]  # 여기를 채워보세요

result = 0
counter = 0
for i in numbers:
    result += i
    counter += 1
average = result / counter
print(average)

#3 range()와 for를 사용해 구구단 3단(3 * 1 ~ 3 * 9)을 출력해보세요.
result=0
a=3
for i in range(1,10):
    print(f"{a}X{i}={a*i}")

#4 max() 함수를 사용하지 않고 반복문으로 최댓값을 찾아보세요.
numbers = [12, 25, 7, 33, 18] 

max=numbers[0]
for number in numbers:
    if max<number:
        max=number
print(max)

#5 dict를 키:값 형태로 한줄 출력
character = {"name": "기사", "hp": 200, "mp": 30, "level": 5}

for key in character:
    print(f"{key}:{character[key]}")

#6 while 반복문으로 1부터 5까지 출력해보세요.
start=1
while True:
    if 5<start:
        break
    print(start)
    start+=1

#7 리스트에서 짝수 개수 세기
numbers = [3, 8, 15, 22, 7, 40, 11]

counter=0
for i in numbers:
    if i%2==0:
        counter+=1
print(counter)

#8 문자열 거꾸로 출력하기
word = "Python"
keyword=list(word)
keyword.reverse()
print(keyword)

#9 57이라는 값이 몇 번째 인덱스에 있는지 break를 사용해 찾아보세요.
array = [273, 32, 103, 57, 52]

end=57
counter=0
while True:
    if array[counter] == end:
        if counter < len(array):
            print(counter)
            break
    counter+=1


#9-2 enumerate 활용
for i,v in enumerate(array): 
    if v==counter:
        print(i)
        break
    else:
        print-1

#10 1부터 100까지의 합 구하기 (while)
i=1
result=0
while i<=100:
    result=result+i
    i+=1
print(result)

#11 구구단 2~9단 전체 출력하기 (중첩 for)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")

#11 구구단 2~9단 전체 출력하기 (중첩 while)
i=2
while i<=9:
    j=1
    while j<=9:
        print(f"{i} x {j}={i*j}")
        j+=1
    i+=1

#12 1부터 30까지 숫자를 출력하되, 3의 배수면 "Fizz"
#   5의 배수면 "Buzz", 둘 다의 배수면 "FizzBuzz"를 출력해보세요.
numbers = list(range(1, 31))
for i in numbers:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#13 짝수만 필터링해서 새 리스트 만들기
numbers = [3, 8, 15, 22, 7, 40, 11, 6]

even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)

#13_1 refactoring(리스트 컴프리헨션)
even_list1=[n for n in numbers if n%2==0]
print(even_list1)

#14 두 리스트로 딕셔너리 만들기 (range 활용)
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

for i in range(len(key_list)):
    character[key_list[i]]=value_list[i]
print(character)

#15 리스트 중복값 제거
numbers = [1, 3, 2, 3, 5, 1, 4, 2]

new=[]
for i in numbers:
    if i not in new:
        new.append(i)
print(new)

#16 별 삼각형 만들기 (오름차순)
for i in range(6):
    print("*"*i)

#17 별 삼각형 만들기 (내림차순, 역삼각형)
for i in range(5,0,-1):
    print("*"*i)

#18 리스트 최댓값/최솟값 동시에 찾기
numbers = [45, 12, 89, 3, 67, 21]

max=numbers[0]
min=numbers[0]
for i in numbers:
    if max<i:
        max=i
    if min>i:
        min=i
print(str(max)+"/"+str(min))

#19 점수표에서 80점 이상인 사람의 이름만 리스트로
scores = {"철수": 85, "영희": 72, "민수": 91, "지은": 68}
for key in scores:
    if scores[key]>=80:
        print(key)

#20 while + break: 누적합이 목표값을 넘는 순간 찾기
#   1부터 순서대로 더해서 합이 처음으로 500을 넘는 순간의 숫자와 그때의 합
result=0
counter=1

while True:
    result+=counter
    counter+=1
    if result > 500:
        break
print(str(counter)+','+str(result))

#21 reverse()나 슬라이싱을 사용하지 않고 반복문으로 반대로 리스트 출력
numbers = [1, 2, 3, 4, 5]

e=len(numbers)-1
re_numvers=[]

while e>=0:
    re_numvers.append(numbers[e])
    e-=1
print(re_numvers)

#22 소수판별
number=17
n=0
prime=True
if prime>2:
    prime=False
while n<number:
    if number%n==0:
        prime=False
        break
    n+=1
if prime:
    print("PRIME")
else:
    print("NOT PRIME")

#23 문자열 내 특정 문자 개수 세기
sentence = "banana"
target = "a"

b=len(sentence)
keyword=list(sentence)
counter=0
print(keyword)
for i in range(b):
    if target==keyword[i]:
        counter+=1
print(counter)

#24 버블 정렬로 리스트 오름차순 정렬하기
numbers = [5, 2, 9, 1, 7]
sort=[]
end=len(numbers)

for i in range(end):
    for j in range(end-1-i):
        if numbers[i]>numbers[j]:
            print()

#25 1부터 50까지의 숫자 중 3의 배수를 제외한 수의 합
n=50
s=0

numbers=list(range(1,n+1))
print(numbers)
for j in numbers:
    if j%3==0:
        continue
    else:
        s+=j
print(s)

#26 딕셔너리 리스트에서 최고 점수 학생 찾기
students = [{"name": "철수", "score": 85},
            {"name": "영희", "score": 92},
            {"name": "민수", "score": 78},]
print(len(students))
score=[]
for student in students:
    for key in student:
        if type(student[key])==int:
            score.append(student[key])
max=score[0]
for i in score:
    if i>max:
        max=i
print(max)

#27 range 3개 매개변수로 짝수의 합
#   range(A, B, C) 형태만 사용해서(if문 없이)



#28 리스트에서 두 번째로 큰 값
#   numbers = [45, 12, 89, 3, 67, 21]



#29 while로 팩토리얼 계산