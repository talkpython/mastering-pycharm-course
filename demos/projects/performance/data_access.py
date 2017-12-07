import time


def get_records(text):
    conn = create_connection()
    results = run_query(conn, text)
    return results


__conn = None


def create_connection():
    global __conn

    if __conn:
        return __conn

    time.sleep(.250)
    __conn = {'connected': True}
    return __conn


def run_query(conn, text):
    if not text:
        return []

    data = []
    for r in range(1, 100):
        row = read_row(conn)
        data.append(row)

    return data


def read_row(conn):
    time.sleep(.00001)  # Improved index!
    if conn.get('connected'):
        return {'col1': 'val1', 'col2': 'val2'}

    raise Exception("No connection")
