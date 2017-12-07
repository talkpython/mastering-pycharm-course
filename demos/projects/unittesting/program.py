import core


def main():
    while True:
        book_event()
        print()


def book_event():
    print("*********************************************")
    print("* TABLE OPEN: Find your dinner reservation! *")
    print("*********************************************")
    print()

    print("What type of food are you in the mood for?")
    print("1. Thai")
    print("2. Burgers")
    print("3. Seafood")
    print("4. Other")
    choice = input("Choose a number: ")
    choice = int(choice)

    options = core.find_available(choice)

    print()
    if not options:
        print("Whoops, no tables for that food type. Try another.")
        return

    print("Here are the open tables:")
    for idx, o in enumerate(options):
        print("{}. Restaurant: {}, table: {}.".format(idx + 1, o.restaurant, o.table_id))

    print()
    num = int(input("Enter a number of the table to book: ")) - 1

    to_book = options[num]
    booked = core.book_table(to_book.table_id)
    print("Booked you a table at {} in table {}".format(booked.restaurant, booked.table_id))


if __name__ == '__main__':
    main()
