def make_chocolate(small, big, goal):
    big_count = min(big, goal // 5)
    remaining = goal - big_count * 5
    if remaining <= small:
        return remaining
    return -1