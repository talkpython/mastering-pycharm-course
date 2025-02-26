import sys

import httpx
from colorama import Fore


def main():
    print('-' * 60)
    print('Talk Python title finder')
    print('-' * 60)
    print(f'Args = {sys.argv}')
    print()

    num: int = get_number()
    title: str = get_title(num)

    print(f'The title for episode {Fore.GREEN}{num} is {Fore.YELLOW}{title}')

    numbers = [1,2,5]
    for i, number in enumerate(numbers):
        print(f"The {i}th number is {number} and title is {get_title(number)}")

    print(f'This is fun! {title}')


def get_number() -> int:
    return int(input("Enter the number of the episode: "))


def get_title(episode_number: int) -> str:
    """
    Fetches the title of a TalkPython episode based on the provided episode number.

    This function constructs an API URL using the given episode number,
    sends a GET request to fetch the episode details, and extracts the
    relevant title information from the response.

    Parameters:
        episode_number (int): The number of the TalkPython episode whose title
                              is to be fetched.

    Returns:
        str: The title of the specified TalkPython episode.

    Raises:
        requests.exceptions.RequestException: If the request fails at the network
                                              or protocol level.
        HTTPError: If the response contains an HTTP error status code.
    """
    # https://talkpython.fm/episodes/show/492/great-tables.title
    url = f'https://talkpython.fm/episodes/show/{episode_number}/any-text-here.title'

    resp = httpx.get(url)
    resp.raise_for_status()

    return resp.text.strip()

if __name__ == '__main__':
    main()
