import core_compute
import data_access
import services


def main():
    # once = False
    for _ in range(1, 10):
        go()
        # input("Time to get a snapshot! ENTER AFTER")


def go():
    text = 'profiling'
    results = services.search(text)
    print('search: {}'.format(results))
    records = data_access.get_records(text)
    print('db: {}'.format(len(records)))
    total = core_compute.compute_analytics(results, records)
    print("The total is: {:,}".format(total))


if __name__ == '__main__':
    main()
