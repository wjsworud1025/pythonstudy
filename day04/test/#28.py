# 리스트에서 두 번째로 큰 값
numbers = [45, 12, 89, 3, 67, 21]

second=numbers[0]
first=numbers[0]
for number in numbers:
    if number>first:
        first=number
for number in numbers:
    if number==first:
        continue
    if number>second:
        second=number
print(f"{first},{second}")