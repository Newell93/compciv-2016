from os.path import join
import json
DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
# boy this is bad practice...but it's fast...
NAMES_DATA_ROWS = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
    # prepare an empty result just in case the given name is not found in our database
    result = { 'name': name, 'gender': None, 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        # find first row...
        if name.lower() == row['name'].lower():
            # this should be the match
            result = row
  
            break
   
    return result
