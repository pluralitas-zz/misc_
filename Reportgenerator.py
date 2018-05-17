# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:48:41 2018

@author: aucheukyan
Report generator for Production server(NUH UNIX) /listmpAS/tmp2/log/listearchive115.del
"""

import datetime
import os
for files in os.walk('.'):
   files = files[2]



#Date
now = datetime.datetime.now() #acquire date information
date = str(now.strftime("%d/%m/%Y")) #formatting the date information
date2 = str(now.strftime("%Y%m%d"))

print('Extract the relevant dataset from Production server(NUH UNIX) /listmpAS/tmp2/log/listearchive115.del into a separate file')
filename = input('What is the file name (full with extension or partial)?:  ')


for fil in files:
    if fil.find(filename) >= 0:
        file = fil

with open(file,'r') as f:
    name = f.read().replace('\n',';')
    
    
name= name.split(';')

#ARC
arc=[]
for i in range(len(name)):
    if name[i].startswith('ARC '):
        arc.append(name[i])
        
        
# Extract Perform Date Time
perdate = arc[0]
perdate = perdate.split(' ')
performdate = perdate[3] + ' ' + perdate[2] + ' ' + perdate[5] + ', ' + perdate[4] + 'hrs'
performdate =performdate.replace(':00','')

# Extract 
numbers= ', '.join(arc)
numbers=numbers.split(' ')

request=[]
bill=[]
technical=[]

for i in range(len(numbers)):
    if numbers[i].startswith('Requests'):
        request=numbers[i+1]
        
for i in range(len(numbers)):        
    if numbers[i].startswith('Bills'):
        bill=numbers[i+1]
        
for i in range(len(numbers)):        
    if numbers[i].startswith('Technical'):
        technical=numbers[i]

technical=technical.replace('Technical:','')
bill=bill.replace(',','')

#Email
title = 'Weekly Archival Report - ' + date

line1 ='Dear all,'
line2 ='This is a daily report regarding the archival of records; requests, bills and technical audits which was performed on ' + performdate + '.'
line3 ='Number of records archived:'
line4 ='Requests:' + request
line5 ='Bills:' + bill
line6 ='Technical Audits:' + bill
line7 ='Attached in this email in the list of access numbers that has been archived.'

emailout = [title , "\r\n", "\r\n", line1 ,'\r\n', line2 , "\r\n" , line3 , line4 , line5 , line6 , "\r\n" , line7]

outF = open("email"+ date2 + ".txt", "w")
for line in emailout:
  # write line to output file
  outF.write(line)
  outF.write("\r\n")
outF.close()

#BILLS
accbills=[]
accnobills=[]

for i in range(len(name)):
    if name[i].startswith('BILL '):
        accbills.append(name[i])

for i in range(len(accbills)):
    accbills[i] = accbills[i].replace('Acc.: ','Acc.: ,')

for i in range(len(accbills)):
    accbills[i] = accbills[i].replace(' RQ1',', RQ1')
    
for i in range(len(accbills)):
    accbills[i] = accbills[i].split(',')

for i in range(len(accbills)):
    accnobills.append(accbills[i][1])

#REQUEST
accrqst=[]
accnorqst=[]
for i in range(len(name)):
    if name[i].startswith('RQST '):
        accrqst.append(name[i])
        
for i in range(len(accrqst)):
    accrqst[i] = accrqst[i].replace('Acc.: ','Acc.: ,')

for i in range(len(accrqst)):
    accrqst[i] = accrqst[i].replace(' RQ1',', RQ1')
    
for i in range(len(accrqst)):
    accrqst[i] = accrqst[i].split(',')

for i in range(len(accrqst)):
    accnorqst.append(accrqst[i][1])
        
#Write rqst to output
outF = open("AccessNumber"+ date2 + ".txt", "w")
for line in accnorqst:
  # write line to output file
  outF.write(line)
  outF.write("\r\n")
outF.close()

#Write bills to output
#outF = open("access number(bills).txt", "w")
#for line in accnobills:
  # write line to output file
#  outF.write(line)
#  outF.write("\r\n")
#outF.close()