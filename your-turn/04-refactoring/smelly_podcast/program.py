import service


def main():
    show_header()
    service.download_data('https://talkpython.fm/episodes/rss')
    latest_show_id, oldest_show_id = service.get_show_id_range()
    print("Working with total of {} episodes".format(latest_show_id))
    display_results(latest_show_id, oldest_show_id)


def display_results(latest_show_id, oldest_show_id):
    start = oldest_show_id
    end = latest_show_id + 1
    for show_id in range(start, end):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
