import random
print("# random module")

# random(): 0.0 <= 1.0 사이의 flot를 리턴
print("- random():", random.random())

# uniform(min, max): 지정한 범위 사이의 flot를 리턴
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int 값을 리턴
# - randrange(max): 0부터 max사이의 값을 리턴
# - randrange(min, max): min부터 max 사이의 값을 리턴
print("- randrange(10):", random.randrange(10))
print("- randrange(10, 15):", random.randrange(10, 15))

# cohice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print("- choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))

# shuffle(list): 리스트 요소들을 랜덤하게 섞음
## shuffle()은 리스트를 그 자리에서(in-place) 섞기 때문에 반환값은 None
### 섞인 결과를 보려면 원본 리스트를 다시 출력
shuffle_list=[1,2,3,4,5]
random.shuffle(shuffle_list)
print("- shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))
print("변경된 셔플 값", shuffle_list)

# sample(list, k='숫자'): 리스트의 요소 중에 k개를 뽑음
print("- sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))