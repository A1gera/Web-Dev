numbers = list(map(int, input().split()))
cnt = 0
for i in range(1, len(numbers) - 1):
    if int(numbers[i])> int(numbers[i-1]) and int(numbers[i])> int(numbers[i+1]):
        cnt+=1
print(cnt)