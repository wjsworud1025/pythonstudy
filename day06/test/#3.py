#짝수/홀수 분류하기 — [제어문 + 반복문]
#1부터 20까지의 숫자 중 짝수는 even_list, 홀수는 odd_list에 각각 담아 출력

even_list=[]
odd_list=[]
for num in range(1,21,+1):
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(f"{even_list} \n {odd_list}")
