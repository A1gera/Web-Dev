numbers = input().split()
cnt = 0
for i in range(len(numbers)):
    if int(numbers[i])> 0:
        cnt +=1
print(cnt)