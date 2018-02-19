import os
import datetime

#Date
now = datetime.datetime.now() #acquire date information
date = str(now.strftime("%Y-%m-%d")) #formatting the date information

#File name input request
file = input('Filename : ')

#Date of making file
text = "! Created on " + date

if not os.path.exists(file):
	os.makedirs(file)

os.chdir(file)
f = open("Work Progress.txt","w+")
f.write(text)
f.close()
