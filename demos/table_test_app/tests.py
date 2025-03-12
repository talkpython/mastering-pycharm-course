import pytest

import core


def test_there_are_available_tables():
    choice = 1
    one_tables = core.find_available(choice)
    assert len(one_tables)


def test_table_can_be_booked():
    table = core.all_tables()[0]

    booked_table = core.book_table(table.table_id)
    #  verify it is booked and is the same as booked.

    assert table.is_booked
    assert table.table_id == booked_table.table_id


def test_cannot_book_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table('not-a-table-id')


def test_cannot_book_booked_table():
    table = core.find_available(2)[0]
    core.book_table(table.table_id)

    with pytest.raises(core.TableUnavailableError):
        print("Pushing our luck!")
        core.book_table(table.table_id)
