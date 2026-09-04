#점수 기준으로 내림차순 정렬하기
scores = [("철수", 85), ("영희", 92), ("민수", 78)]


d=dict(scores)              #1단계 딕셔너리로 재구성, dict() 생성자 활용하여 재구성
l=[]                        #sort한 데이터를 저장할 리스트를 구성
for k, v in d.items():      #재구성한 딕셔너리의 item을 하나씩 호출
	l.append((v, k))        #sort 데이터를 저장할 공간에 아이템을 추가하는데,
l.sort(reverse=True)        #reverse=True 함수를 활용하여 재구성한 딕셔너리를 반전
sorted_scores={}            #최종 소팅된 스코어를 저장할 빈 딕셔너리 구성
for v, k in l:              #재구성한 리스트에서 키와 벨류를 받아
	sorted_scores[k]=v      #dict[key]=value 함수를 통해 값을 저장
print(sorted_scores)


#방법2 
scores_dict = dict(scores)
print(scores_dict)
#def 선언
def get_score(item):
    return item[1]
scores_dict = dict(scores_dict.items(), key=get_score,reverse=True)
print(scores_dict)