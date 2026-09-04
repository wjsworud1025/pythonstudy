# dict를 키:값 형태로 한 줄 출력
character = {"name": "기사", "hp": 200, "mp": 30, "level": 5}

for key in character:                   #dict에서 키라는 값으로 data를 한개씩 호출
    print(f"{key}:{character[key]}")    #1개 data = "name": "기사" / 단 호출은 벨류값을 가져오지 않는다.
                                        #for문에서 불러온 key 값과 key 값에 대응하는 벨류값을 가져와 출력
