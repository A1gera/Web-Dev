binary_num = input()
decimal_num = 0
for i in range(len(binary_num)):
    digit = int(binary_num[i])
    decimal_num += digit * (2 ** (len(binary_num) - i - 1))
print(decimal_num)
