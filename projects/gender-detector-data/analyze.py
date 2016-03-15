from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
from os import makedirs
DATA_DIR = 'tempdata'
CLASSIFIED_DIR = join(DATA_DIR, 'classified')
DATA_FILE_BASENAME = 'guests-simpsons.csv'
FULL_DATA_FILENAME = join(CLASSIFIED_DIR, DATA_FILE_BASENAME)
joe = open(FULL_DATA_FILENAME, 'r')
First_rows = list(DictReader(joe))
joe.close()
simpsons = {'M': 0, 'F': 0, 'NA': 0}
for row in First_rows:
    wiggum = row['gender']
    simpsons[wiggum] += 1
print("F:", simpsons['F'], "M:", simpsons['M'])

for x in range(1,27):
    yr = str(x)
    print("Season", yr)
    byseason = {'M': 0, 'F': 0, 'NA': 0}
    for row in First_rows:
        if yr == row['Season']:
            wiggum = row['gender']
            byseason[wiggum] += 1
    print("F:", byseason['F'], "M:", byseason['M'])

for x in range(1,27):
    yr = str(x)
    print("Season", yr)
    ratioseason = {'M': 0, 'F': 0, 'NA': 0}
    for row in First_rows:
        if yr == row['Season']:
            wiggum = row['gender']
            ratioseason[wiggum] += 1
    print("Ratio of M/F Guests:", round(ratioseason['M'] / ratioseason['F']))
