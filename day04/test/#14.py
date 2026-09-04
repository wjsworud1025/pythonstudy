# 두 리스트로 딕셔너리 만들기 (range 활용)
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}                                      #출력을 위한 빈 dict

for index in range(len(key_list)):                  #len()함수로 몇개의 리스트를 탐색할지 확인하여 index로 data 호출
    character[key_list[index]] = value_list[index]  #dict"키값"="밸류" 명령어로 for 구문으로 나오는 각 데이터를 매칭
print(character)                                    #매칭된 최종 dict를 출력 
