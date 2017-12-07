import pytest
import core


def test_there_are_tables_available():
    choice = 1
    one_tables = core.find_available(choice)

    assert len(one_tables)


def test_table_can_be_booked():
    tables = core.all_tables()

    table = tables[0]
    booked = core.book_table(table.table_id)

    assert booked
    assert booked.is_booked
    assert booked.table_id == table.table_id


def test_cannot_book_a_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table('not an ID!')


def test_cannot_book_a_booked_table():
    tables = core.all_tables()

    core.book_table(tables[1].table_id)
    with pytest.raises(core.TableUnavailableError):
        core.book_table(tables[1].table_id)
