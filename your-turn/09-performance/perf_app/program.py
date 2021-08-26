import core_compute
import data_access
import services


def main():
    for _ in range(1, 10):
        go()


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
