# 버블 정렬로 리스트 오름차순 정렬하기
numbers = [5, 2, 9, 1, 7]

for end in range(len(numbers) - 1, 0, -1):
    for index in range(end):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
print(numbers)
