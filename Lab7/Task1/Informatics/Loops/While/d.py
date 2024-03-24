n = int(input())
while n>1:
    if n%2 ==1:
        print("NO")
        break
    else:
        n //=2
else: print("YES")