import json

def load_data(filepath='data/moz_culture_data.json'):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
