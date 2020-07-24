#!/usr/bin/env python3

import re
import sys 

password = sys.argv[1]

def detect_password(password):
	#a strong password must have atleast 1 Uppercase, 1 lowercase ,a number and a special character in any order
	pattern = r'.*[(A-Z)]+.*[(a-z)]+.*[(0-9)]+.*[(!@#$%^&*-_+=)]+.*'
	result = re.search(pattern,password)
	if(result != None):
		print('Strong Password')
	else:
		print('Weak Password')

detect_password(password)
