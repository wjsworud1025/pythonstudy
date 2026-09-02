#84 기초 종합 소리 파일 저장용량 계산
h,b,c,s=map(int,(input().split()))
bit=h*b*c*s
mb=bit/8/1024/1024
print("{:.1f} MB".format(mb))
