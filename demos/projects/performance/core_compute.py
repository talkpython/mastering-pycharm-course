import math
import time


def compute_analytics(search, rows):
    search_data = read_data(search)
    db_data = read_data(rows)

    total = learn(search_data, db_data)
    return total


def read_data(data):
    for _ in range(0, len(data)):
        time.sleep(.005)

    return data


def learn(search_data, db_data):
    total = 0
    for ids, s in enumerate(search_data):
        for idd, d in enumerate(db_data):
            for r in range(1, 100):
                val1 = ids * idd * len(s)
                val2 = math.pow(idd, 7)

                res = math.sqrt(val1 * val1 + val2 * val2)
                mod = math.pow(-1, ids + r)

                total += res * mod

    return total
