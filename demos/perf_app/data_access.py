import functools
import time


def get_records(text):
    conn = create_connection()
    results = run_query(conn, text)
    return results


def create_connection():
    time.sleep(.250)
    return {'connected': True}


def run_query(conn, text):
    if not text:
        return []

    data = []
    for r in range(1, 100):
        row = read_row(conn)
        data.append(row)

    return data


def read_row(conn):
    time.sleep(.0001) # todo: improve index!
    if conn.get('connected'):
        return {'col1': 'val1', 'col2': 'val2'}

    raise Exception("No connection")
