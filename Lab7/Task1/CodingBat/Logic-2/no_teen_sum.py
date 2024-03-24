def check_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    else:
        return n

def no_teen_sum(a, b, c):
    return check_teen(a) + check_teen(b) + check_teen(c)
