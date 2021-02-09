from typing import List


def remove_pet(k: List[str], name: str):
    return [
        p
        for p in k
        if p != name
    ]


kennel = ['Snoopy', 'Fido', 'Fido', 'Pluto']
result = remove_pet(kennel, 'Fido')

print(result)
