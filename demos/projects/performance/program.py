import core_compute
import data_access
import services


def main():
    go()


def go():
    text = 'profiling'
    results = services.search(text)
    print('Talk Python search results:')
    for r in results:
        print(r[:100].strip() + '...')

    records = data_access.get_records(text)
    print('db: {}'.format(len(records)))
    total = core_compute.compute_analytics(results, records)
    print("The total is: {:,}".format(total))


if __name__ == '__main__':
    main()
