# 점수표에서 80점 이상인 사람의 이름만 리스트로
scores = {"철수": 85, "영희": 72, "민수": 91, "지은": 68}

for name in scores:             #dict 에서 name으로 리스트를 호출(dict에서 직접 호출할때는 key값만 호출된다.)
    if scores[name] >= 80:      #호출된 key값으로 dict["key"] 구문을 통해 value값을 가져와 기준 점수와 비교
        print(name)             #최종 기준점수를 통과한 key값을 출력
