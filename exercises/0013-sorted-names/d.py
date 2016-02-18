from os.path import join
import operator
records_list = []
dudes =[]
gals =[]
f = open("tempdata/ssa-babynames-nationwide-2014/babies", 'r')
for line in f:
    name, sex, babies = line.strip().split(',')
    if "x" in name:
    	row = [name, sex, int(babies)]
    	records_list.append(row)

for sex in records_list:
	if "M" in sex:
		row = [name, sex, int(babies)]
		dudes.append(row)


for sex in records_list:
	if "F" in sex:
		row = [name, sex, int(babies)]
		gals.append(row)
odudes = sorted(dudes, key=operator.itemgetter(2), reverse=True)
for x in range(5):
	print(odudes[x][0].ljust(11), str(odudes[x][1]).rjust(13), sep = '')
ogals = sorted(gals, key=operator.itemgetter(2), reverse=True)
for x in range(5):
	print(ogals[x][0].ljust(11), str(ogals[x][1]).rjust(13), sep = '')

#def sort_foo(x):
 #  return x[2]
#sorted(dudes, key=sort_foo, reverse=True)
#for x in dudes[0:9]:
 # print (x)

#def sort_foo(x):
#   return x[2]
#sorted(gals, key=sort_foo, reverse=True)
#for x in gals[0:9]:
#  print (x)







#for sex in records_list:
#	if records_list[sex]+='F'
#	females.append(row)
#	print(females)
    	




    	#row = [name, sex, int(babies)]
   		#records_list.append(row)









#def sort_foo(x):
 #   return x[2]
#sorted(f, key=sort_foo, reverse=True)
#print(records_list[0])