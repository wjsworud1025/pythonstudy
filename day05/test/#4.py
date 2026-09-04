#리스트에서 특정 값의 위치와 개수 찾기
#"apple"이 리스트에서 처음 등장하는 인덱스(위치)와, 총 몇 번 등장하는지(개수)
fruits = ["apple", "banana", "apple", "cherry", "apple"]
num=fruits.index("apple")
counter=0
for i in fruits:
    if i=="apple":
       counter+=1
print(f"{num}/{counter}") 

#리스트 컴프리헨션(List Comprehension) 방식
apple_idx=next(i for i, v in enumerate(fruits) if v == "apple")
apple_count=sum(1 for v in fruits if v== "apple")
print(apple_idx," ",apple_count)