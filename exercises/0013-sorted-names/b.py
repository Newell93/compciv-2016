records_list = []
f = open("tempdata/ssa-babynames-nationwide-2014/babies", 'r')
for line in f:
    name, sex, babies = line.strip().split(',')
    row = [name, sex, int(babies)]
    records_list.append(row)
def sort_foo(x):
    return x[2]
sorted(f, key=sort_foo, reverse=True)
print(records_list[0],records_list[1],records_list[2],records_list[3],records_list[4],records_list[5],records_list[6],records_list[7],records_list[8],records_list[9])