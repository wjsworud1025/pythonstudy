import os

print("현재 운영체제:", os.name)
print("현재폴더:", os.getcwd)
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다(폴더가 비어있을 때만 제거 가능).
os.mkdir("hello")   #make directory
os.rmdir("hello")   #remove directory

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")

# os.unlink("new.txt")   # remove()와 완전히 동일한 함수(이름만 다름)

# 시스템 명령어 실행
os.system("dir")