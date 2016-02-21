#got this from github (posted answers) i understand it now, please don't give me credit for it since it was only complete after i checked github answers
from os.path import join
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
mx = fx = 0
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        if sex == 'F':
            fx += int(babies)
        else:
            mx += int(babies)
print("F:", fx)
print("M:", mx)