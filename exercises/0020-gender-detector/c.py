from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'
alltxtfiles_path = join(DATA_DIR, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)
a_filename = 'tempdata/yob1951.txt'
bname = basename(a_filename)
year = bname[3:7]
myfilenames = []
for fname in alltxtfiles_names:
  bname = basename(fname) 
  year = bname[3:7]       
  if year >= "1950":
      myfilenames.append(fname)
totalsdict = {'M': 0, 'F': 0}
tally = {'M': set(), 'F': set()}
for fname in glob(join(DATA_DIR, '*.txt')):
    # doing the filtering if filenames in one loop
    year = basename(fname)[3:7]
    if year >= "1950":
        for line in open(fname, 'r'):
            name, gender, babies = line.split(',')
            tally[gender].add(name)
f_to_m_ratio = round(100*(len(tally['F']) / len(tally['M'])))
print("F:", (len(tally['F'])), "M:", (len(tally['M'])))

print(f_to_m_ratio)
