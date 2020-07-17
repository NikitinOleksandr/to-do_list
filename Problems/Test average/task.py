def average_mark(*args):
    total = 0
    count = 0
    for arg in args:
        total += arg
        count += 1
    average = total / count
    return round(average, 1)
