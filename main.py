#!/usr/bin/env python
import time
from PIL import ImageOps
# from PIL import ImageGrab
import pyscreenshot as ImageGrab
from datetime import datetime
import os
# from numpy import *
#build instructions
# sudo apt-get install python-imaging
# easy_install pyscreenshot

i = 0

while(1):
	time_date_str =  str(datetime.now())
	time_date_str = time_date_str.split(" ")
	date = str(time_date_str[0])
	time_t = str(time_date_str[1][:-7])
	im = ImageOps.grayscale(ImageGrab.grab())
	# im.show()
	folder_name = './'+date
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	os.chdir(folder_name)	
	#this part is for adding which part of day
	parts_of_day = time_t.split(':')

	if(int(parts_of_day[0])>=00 and int(parts_of_day[00])<=11):
		sub_folder_name = '00-12'
	else:
		sub_folder_name = '12-00'

	sub_folder_path = './'+sub_folder_name

	if not os.path.exists(sub_folder_path):
		os.mkdir(sub_folder_path)
	os.chdir(sub_folder_path)
	file_name = time_t+'.jpg'
	im.save(file_name, quality=25)
	# os.system('cd .. > /dev/null 2>&1')
	# os.system('cd .. > /dev/null 2>&1')
	abc =  os.getcwd()
	# print abc
	abc = abc.rpartition('/')[0]
	abc = abc.rpartition('/')[0]
	# print abc
	os.chdir(abc)
	# print '***'
	time.sleep(5)
	#print datetime.now()
	#print i 
	#i=i+1
