numbers = input().split()

for i in range(1, len(numbers)):
    if int(numbers[i])> int(numbers[i-1]):
        print(numbers[i], end=" ")