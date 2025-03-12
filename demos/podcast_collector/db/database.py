import json
from pathlib import Path

podcasts: list[dict] = []

def load_data():
    global podcasts
    db_file = Path(__file__).parent / 'data.json'

    podcasts = json.loads(db_file.read_text()).get('podcasts')

load_data()
