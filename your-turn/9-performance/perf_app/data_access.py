import time


def get_records(text):
    conn = create_connection()
    results = run_query(conn, text)
    return results


# TODO: Make this faster by caching / reusing the connection
def create_connection():
    time.sleep(.250)
    conn = {'connected': True}
    return conn


def run_query(conn, text):
    if not text:
        return []

    data = []
    for r in range(1, 100):
        row = read_row(conn)
        data.append(row)

    return data


def read_row(conn):
    time.sleep(.001)  # TODO: Improved index, i.e. shorting thiis!
    if conn.get('connected'):
        return {'col1': 'val1', 'col2': 'val2'}

    raise Exception("No connection")
