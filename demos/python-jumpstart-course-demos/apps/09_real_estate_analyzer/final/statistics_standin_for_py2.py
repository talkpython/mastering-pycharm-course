def mean(data):
    total = 0.0
    count = 0
    for x in data:
        count += 1
        total += x

    return total / max(1, count)
