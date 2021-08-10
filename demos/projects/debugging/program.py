import math_tricks
# 1,1,2,3,5,8,13,21,...

data = []

fibs = math_tricks.fibonacci()
odd_fibs = math_tricks.odd_numbers(fibs)

for o in odd_fibs:
    if o > 1000:
        break

    data.append(o)

print(data)
