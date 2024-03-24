numbers = input().split()

for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        print(numbers[i], end=" ")
