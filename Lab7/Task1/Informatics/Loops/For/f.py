x = int(input())
rev=""
for i in str(x):
    rev = i + rev
print(rev.lstrip("0")) 
