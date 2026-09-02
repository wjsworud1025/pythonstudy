#현재 시간을 시스템으로 부터 가져와서 오전, 오후인지 판단
# 오전, 오후의 기준 12시로 정한다.
#elif(), format(), split() 활용

import datetime
current_time = datetime.datetime.now()

if current_time.hour < 12:
    print("오전")
elif current_time.hour >= 12:
    print("오후")

format_time = current_time.strftime("%H:%M:%S")
print("현재 시간:", format_time)

