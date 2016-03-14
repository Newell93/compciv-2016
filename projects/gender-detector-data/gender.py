from os.path import join
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
NAMES_DATA_ROWS = open(WRANGLED_DATA_FILENAME)
def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if int(name.lower() == row['name'].lower()):
            result = row
            break
    return result
