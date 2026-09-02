#85 기초 종합 그림 파일 저장용량 계산
w,h,b=map(int,input().split())
size=w*h
bit=size*b
mb=bit/8/1024/1024
print("{:.2f} MB".format(mb))
