# 파일처리
# - 텍스트 파일
# - 바이너리 파일

# 파일을 처리하려면?? 
# 1. 파일을 열기 (open) > 파일을 읽기, 파일을 쓰기
    # - open(파일의 경로, mode)
    # mode: w, a, r (write, append, read)
    # - close()
    # - with 키워드: 파일을 열고 닫지 않는 실수를 방지하기 위한 태그

file = open("basic.txt","w")
file.write("파이썬 파일 처리 예제 작성중....")
file.close()