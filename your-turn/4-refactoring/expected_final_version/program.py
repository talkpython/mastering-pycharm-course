from service import get_episode, get_latest_show_id, download_data, get_min_show_id


def main():
    show_header()

    download_data()

    latest_show_id = get_latest_show_id()

    print("Working with total of {} episodes".format(latest_show_id))

    display_results()


def display_results():
    # DISPLAY RESULTS
    start = get_min_show_id()
    end = get_latest_show_id()

    for show_id in range(start, end):
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
