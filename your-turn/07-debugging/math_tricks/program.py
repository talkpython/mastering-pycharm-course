import core


data = []

fibs = core.fibonacci()
odd_fibs = core.odd_numbers(fibs)

for o in odd_fibs:
    if o > 1000:
        break

    data.append(o)

print(data)
