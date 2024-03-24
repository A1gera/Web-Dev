answer_system = int(input())
answer_student = int(input())
if answer_system == 1 and answer_student != 1:
    print("NO")
elif answer_student == 1 and answer_system != 1:
    print("NO")
else:
    print("YES")
