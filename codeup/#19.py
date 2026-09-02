#19 input+sep 연월일 입력받아 순서 바꿔 출력하기(sep가 공백을 없애고 -로 출력)
y, m, d = input().split('.')
print(d, m, y, sep='-')
