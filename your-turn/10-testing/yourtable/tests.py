import pytest
import core


def test_there_are_tables_available():
    assert False, "Use core to find_available by choice, make sure there is at least one"


def test_table_can_be_booked():
    assert False, "Get a table (all tables), book it by ID, verify it is booked"


def test_cannot_book_a_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        # TODO: verify you cannot book a nonexistant table
        pass


def test_cannot_book_a_booked_table():
    with pytest.raises(core.TableUnavailableError):
        # TODO: verify you cannot book a table that is already booked
        pass
