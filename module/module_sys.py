#명령 매개변수는 실무에서 자주 쓰입니다.
## 예: python module_sys.py filename.txt 처럼 파일 경로 등을 외부에서 지정 가능

# 모듈을 읽어들입니다..

import sys # 명령 매개변수를 출력
print(sys.argv)
print("-"*10)

#컴퓨터 환경과 관련된 정보를 출력
print("getwindowsversion():", sys.getwindowsversion())
print("-"*10)
print("copyright:", sys.copyright)
print("-"*10)
print("version:", sys.version)
# 프로그램을 강제로 종료
sys.exit()