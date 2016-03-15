from os.path import join
import csv
WRANGLED_DATA_FILENAME = join('tempdata', 'wrangledbabynames.csv')
NAMES_DATA_ROWS = list(csv.DictReader(open(WRANGLED_DATA_FILENAME)))
def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result
#for r in NAMES_DATA_ROWS:
#    r['total'] = int(r['total'])
#    r['males'] = int(r['males'])
#    r['females'] = int(r['females'])
#    r['ratio'] = int(r['ratio'])