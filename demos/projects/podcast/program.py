import service


def main():
    print("Welcome to the talk python info downloader.")
    print()

    service.download_info()

    for show_id in range(100, 130):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


if __name__ == '__main__':
    main()
