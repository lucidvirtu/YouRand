"""
Created on Thu Aug  1 23:38:24 2019

@author: lucidvirtu
"""

import webbrowser as wb
import random

char_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
base_url = "https://youtube.com/watch?v="
decision = True
while decision is True:
	vid = ""
	for x in range(11):
		vid = vid+(random.choice(char_list))

	full_url = base_url+vid
	print (full_url)
	wb.open(full_url)
	
	inp = input("Try again? y/n: > ")
	
	if (inp == 'y' or inp == 'Y'):
		decision = True
	else: print("Thank you for playing");decision = False
