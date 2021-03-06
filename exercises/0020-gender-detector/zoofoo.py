from os.path import join
import json
DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
NAMES_DATA_ROWS = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
    result = { 'name': name, 'gender': None, 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
  
            break
   
    return result
