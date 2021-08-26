def fibonacci():
    nxt, current = 1, 0
    while True:
        current, nxt = nxt, nxt + current
        yield current


def odd_numbers(series):
    for n in series:
        if n % 2 == 1:
            yield n
