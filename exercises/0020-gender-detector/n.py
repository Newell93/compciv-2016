from zoofoo import detect_gender
NAMES_TO_TEST = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']
for name in NAMES_TO_TEST:
	print((detect_gender(name)['name']), (detect_gender(name)['gender']), (detect_gender(name)['ratio']))
print("Total:")


		#(detect_gender(name)['gender']), (detect_gender(name)['ratio']))






	#print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
	#print('females:', babycount['females'], 'males:', babycount['males'])