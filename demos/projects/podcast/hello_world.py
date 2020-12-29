def hello(name: str) -> None:
    print("Hello", name)


def list_range(num_list: list) -> None:
    for i, num in enumerate(num_list):
        print("{} :- {}".format(i, num))

def this_test(name='clear'):
    print(name)


if __name__ == '__main__':
    hello('Chinu')
    hello('Samir')
    this_test(name='Chinku')
    list_range([0, 1, 1, 2, 3, 5, 8, 13, 21])

