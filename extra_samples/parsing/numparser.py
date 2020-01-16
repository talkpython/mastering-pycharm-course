from typing import List


def parse(text: str) -> List[int]:
    """
    Parse a string and convert it to a list of integers.
    TODO: Add space char support
    """
    result = []
    for num in text.split(','):
        if '-' in num:
            start, end = num.split('-')
            # FIXME: Support half-open intervals.
            # This comment isn't tracked.
            result.extend(range(int(start), int(end)+1))
        else:
            result.append(int(num))

    return result
