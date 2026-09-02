#98 개미의 미로찾기
b = []
for i in range(10):
    b.append([])
    for j in range(10):
        b[i].append(0)
for i in range(10):
    wall = list(map(int, input().split()))
    for j in range(10):
        b[i][j] = wall[j]
#start
x=1
y=1
while True:
    if b[x][y] == 2:
        x + 7
        y + 7
    b[x][y] = 9
    if b[x][y + 1] != 1:
        y += 1
    elif b[x + 1][y] != 1:
        x += 1
    else:
        break
for i in range(10):
    for j in range(10):
        print(b[i][j], end=" ")
    print()
