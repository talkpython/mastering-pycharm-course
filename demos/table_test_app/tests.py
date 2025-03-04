import pytest
import core


def test_there_are_available_tables():
    choice = 1
    one_tables = core.find_available(choice)
    assert (len(one_tables))


def test_table_can_be_booked():
    ... # Get a table, book it, verify it is booked and is the same as booked.


def test_cannot_book_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table("not-a-table-id")


def test_cannot_book_booked_table():
    ... # Get a table for 2, book it, book it again. :)
