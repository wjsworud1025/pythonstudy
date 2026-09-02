#96
d = []
for i in range(19):
    d.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(19):
        d[x][j] = 1 - d[x][j]
    for j in range(19):
        d[j][y] = 1 - d[j][y]
for i in range(19):
    print(*d[i])
