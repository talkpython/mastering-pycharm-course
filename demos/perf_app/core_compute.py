import time
import math



def compute_analytics(search, rows):
    search_data = read_data(search)
    db_data = read_data(rows)

    # t0 = datetime.datetime.now()

    total = learn(search_data, db_data)

    # dt = datetime.datetime.now() - t0
    # print("Speed: {:,}".format(dt.total_seconds() * 1000))
    return total


def read_data(data):
    for _ in range(0, len(data)):
        time.sleep(.002)  # convert to numpy

    return data


# use as a decorator.
def list_momento(wrapped_list_func):
    cache = {}

    def wrapper(*lists):
        key = ""
        for l in lists:
            key += str(l)

        if key in cache:
            return cache[key]

        val = wrapped_list_func(*lists)
        cache[key] = val

        return val

    return wrapper


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
