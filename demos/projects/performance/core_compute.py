import functools
import time
import math

import datetime


def compute_analytics(search, rows):
    search_data = read_data(search)
    db_data = read_data(rows)

    total = learn(search_data, db_data)
    return total


def read_data(data):
    for _ in range(0, len(data)):
        time.sleep(.0001)  # switch to NumPy

    return data


def list_momento(func):
    cache = {}

    def wrapper_func(*lists):
        # Use a hash rather than full text for key
        key = "KEY: " + ",".join([str(l) for l in lists])
        key = hash(key)

        if key in cache:
            return cache[key]

        cache[key] = func(*lists)
        return cache[key]

    return wrapper_func


@list_momento
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
