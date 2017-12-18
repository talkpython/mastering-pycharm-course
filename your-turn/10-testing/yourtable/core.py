import uuid
from typing import List, Optional


class Table:
    def __init__(self, table_id: str, restaurant: str, food_type: int):
        self.restaurant = restaurant
        self.table_id = table_id
        self.type = food_type
        self.is_booked = False


class EntityNotFoundError(Exception):
    pass


class TableUnavailableError(Exception):
    pass


def find_available(choice: int) -> List[Table]:
    global tables

    return [
        t
        for t in tables
        if t.type == choice and not t.is_booked
    ]


def book_table(table_id: str):
    table = find_table_by_id(table_id)
    if not table:
        raise EntityNotFoundError("No table with this id")

    if table.is_booked:
        raise TableUnavailableError("Table is booked")

    table.is_booked = True
    return table


def all_tables():
    return tables[:]


def find_table_by_id(table_id: str) -> Optional[Table]:
    return table_lookup.get(table_id)


def _id():
    return str(uuid.uuid4())


tables = [
    Table(_id(), "Thai Roses", 1),
    Table(_id(), "Thai Roses", 1),

    Table(_id(), "Siam Thai", 1),

    Table(_id(), "Skyline Burgers", 2),

    Table(_id(), "Little Big Burger", 2),
    Table(_id(), "Little Big Burger", 2),
    Table(_id(), "Little Big Burger", 2),

    Table(_id(), "Jake's Seafood", 3),
    Table(_id(), "Jake's Crawfish", 3),
    Table(_id(), "Portland City Grill", 3),

    Table(_id(), "Waffle Window", 4),
    Table(_id(), "Slappy Cakes", 4),
    Table(_id(), "Slappy Cakes", 4),
]

table_lookup = {
    t.table_id: t
    for t in tables
}
