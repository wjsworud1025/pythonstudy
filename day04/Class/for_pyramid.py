output = ""
for i in range(1, 15):
    for j in range(14, i, -1):
        output += ' '
    for k in range(0, 2 * i - 1):
            output += '*'
            output += '\n'
print(output)


# 중첩 반복문의 안쪽 반복문 역할은 사실 
# output += ("*" * i) 로도 대체할 수 있습니다.
output = ""
for i in range(1, 10):
    output += ("*" * i)
    output += "\n"
print(output)