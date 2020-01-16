from typing import List


def parse(text: str) -> List[int]:
    result = []
    for num in text.split(','):
        if '-' in num:
            start, end = num.split('-')
            result.extend(range(int(start), int(end)+1))
        else:
            result.append(int(num))

    return result
