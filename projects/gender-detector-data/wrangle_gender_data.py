from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
START_YEAR = 1950
END_YEAR = 2014
years = list(range(START_YEAR, END_YEAR, 10))
years.append(END_YEAR)
namesdict = {}
for year in years:
    filename = join(DATA_DIR, 'yob' + str(year) + '.txt')
    print("Parsing", filename)
    with open(filename, 'r') as thefile:
        for line in thefile:
            name, gender, count = line.split(',')
            if not namesdict.get(name): 
                namesdict[name] = {'F': 0, 'M': 0}
            namesdict[name][gender] += int(count)

padjo = []
for name, babiescount in namesdict.items():
    xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
    padjo.append(xdict)


wfile = open(WRANGLED_DATA_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
wcsv.writeheader()
def xfoo(xdict):
    return (-xdict['total'], xdict['name'])

for row in sorted(padjo, key=xfoo):
    wcsv.writerow(row)
wfile.close()
