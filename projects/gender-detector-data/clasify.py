from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'tempdata'
CLASSIFIED_DIR = join(DATA_DIR, 'classified')
makedirs(CLASSIFIED_DIR, exist_ok=True)
DATA_FILE_BASENAMES = ['guests-simpsons.csv']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
NAMES_DATA_ROWS = list(DictReader(open(WRANGLED_DATA_FILENAME)))

def extract_usable_name(First):
    return First

for fname in DATA_FILE_BASENAMES:
    full_filename = join(DATA_DIR, fname)

    xf = open(full_filename, 'r')
    First_rows = list(DictReader(xf))
    xf.close()

    classified_headers = list(First_rows[1]) + ['gender', 'ratio', 'usable_name']
    # start the classified data file
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
        # skip rows in which row['Employee Name'] is "Not provided"
        if "Not provided" in first_name:
            pass
        else:
            usablename = extract_usable_name(first_name)
            xresult = detect_gender(usablename)
            row['gender'] = xresult['gender']
            row['ratio'] = xresult['ratio']
            row['usable_name'] = usablename
            # write to the csv file
            output_csv.writerow(row)
    outfile.close()

