''' table_to_csv.py
	Seng 265 Summer 2016
	Brandon Vickery
	07/22/16
'''

import sys
import re

text = sys.stdin.read().replace('\n',' ')
tables = re.findall(r'<table(?:\s*|\w*|[="%:]*)*>(.*?)</table\s*>',text,re.IGNORECASE)
i = 1

for table in tables:
	final_copy =[]
	row = re.findall(r'<tr(?:\s*|\w*|\W*)*>(.*?)</tr\s*>',table,re.IGNORECASE)

	for r in row:
		cells = re.findall(r'<(?:td|th)(?:\s*|\w*|(?=\W*)|[^>])*>(.*?)</(?:td|th)\s*>',r,re.IGNORECASE)

		temp = []
		for c in cells:
			temp.append((re.sub(r'\s+',' ',c)).strip())
		final_copy.append(temp)
		
	print("TABLE %d:"%(i))
	i += 1
	length = max(len(x) for x in final_copy)
		
	for x in final_copy:
		while(len(x) < length):
			x.append("")
		print(','.join(x))
	print("")