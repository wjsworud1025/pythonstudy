 # 매개변수 1개 - 0부터 A-1까지
a = range(5)
print(a)

# range(0, 5)
print(list(a))

# [0, 1, 2, 3, 4]

# 매개변수 2개 - A부터 B-1까지
print(list(range(0, 5)))
# [0, 1, 2, 3, 4]

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

# 매개변수 3개 - A부터 B-1까지 C씩 증가
print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

# 0부터 10까지(10 포함)를 명시적으로 강조하고 싶을 때
a = range(0, 10 + 1)
print(list(a))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

