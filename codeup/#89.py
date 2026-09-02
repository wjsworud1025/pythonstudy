#89 기초 종합 수 나열 2(등비)
a, r, n = map(int, input().split())
result = a
for i in range(n - 1):
    result *= r
print(result)
