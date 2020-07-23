#!/usr/bin/env python3

import re
import sys

def detect_details(log_file):
	report = []
	with open(log_file) as file:
		
		for line in file:
			if '[WARN]' not in line and '[FATAL]' not in line:
				continue
			#print(line)
			pattern = r' (\w+) \[(\w+)\] ([(\w+) ]+) (\d+)$' 
			id = re.search(pattern,line)
		
			s = id[2] + ':' + id[3] +' '+ id[4] + ', User:' + id[1]
			report.append(s)
	return(report)
def write_details(report):
	file = open('generated_report.txt','w+')
	for s in report:
		file.write(s+'\n')
	file.close()

log_file = sys.argv[1]
result = []
result = detect_details(log_file)
write_details(result)
