# 2
pets = [    {"name": "구름", "age": 5},    {"name": "초코", "age": 3},    {"name": "아지", "age": 1},    {"name": "호랑이", "age": 1}]
print("# 우리 동네 애완 동물들")
for data in pets:
    print(data['name'],str(data['age'])+'살')

#3
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for number in numbers:
    counter[number]=0
for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
print(counter)

#4
character = {    "name": "기사",    "level": 12,    "items": {        "sword": "불꽃의 검",        "armor": "풀플레이트"    },    "skill": ["베기", "세계 베기", "아주 세계 베기"]}

# character의 키를 하나씩 가져옵니다.
for key in character:
    if key=="name":
        result=[]

    value=character[key]
    if type(value) is dict:
        for inner_key in value:
            result.append(f"{inner_key} : {value[inner_key]}")
    elif type(value) is list:
        for item in value:
            result.append(f"{key} : {item}")
    else:
        result.append(f"{key} : {value}")
print(*result,sep="\n")