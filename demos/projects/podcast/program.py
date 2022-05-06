import service

__VERSION__ = "2.1"


def main():
    print_header()
    service.download_info()
    show_titles()




def print_header():
    print("------------------------------------------")
    print(f" THIS PYTHON PODCAST DOWNLOADER v{__VERSION__}")
    print("------------------------------------------")


def show_titles():
    start = service.get_min_episode_id()
    end = service.get_max_episode_id()

    for episode_id in range(start, end + 1):
        show_episode_details(episode_id)


def show_episode_details(episode_id: int):
    episode = service.get_details(episode_id)
    print(f'{episode.id}. -> {episode.title}')


if __name__ == '__main__':
    main()
