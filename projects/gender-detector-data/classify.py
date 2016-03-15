#Dan: I used California Colleges as a template. Thank you for sharing it. 
from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'tempdata'
CLASSIFIED_DIR = join(DATA_DIR, 'classified')
makedirs(CLASSIFIED_DIR, exist_ok=True)
DATA_FILE_BASENAMES = ['guests-simpsons.csv']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')

def extract_usable_name(First):
    return First

for fname in DATA_FILE_BASENAMES:
    full_filename = join(DATA_DIR, fname)

    joe = open(full_filename, 'r')
    First_rows = list(DictReader(joe))
    joe.close()

    classified_headers = list(First_rows[0]) + ['gender', 'ratio', 'usable_name']
    classified_filename = join(CLASSIFIED_DIR, fname)
    print("About to classify", len(First_rows), 'rows into the file:', classified_filename)

    outfile = open(classified_filename, 'w')
    output_csv = DictWriter(outfile, fieldnames=classified_headers)
    output_csv.writeheader()
    xc = 0
    for row in First_rows:
        xc += 1
        first_name = row['First']
        print("On row", xc, first_name)
        if "N/A" in first_name:
            pass
        else:
            usablename = extract_usable_name(first_name)
            get = detect_gender(usablename)
            row['gender'] = get['gender']
            row['ratio'] = get['ratio']
            row['usable_name'] = usablename
            # 
            output_csv.writerow(row)
    outfile.close()
#Dan: I used California Colleges as a template. Thank you for sharing it. 
