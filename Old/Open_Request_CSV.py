
Skip to content
This repository

    Pull requests
    Issues
    Marketplace
    Explore

    @pluralitas

0
0

    0

pluralitas/misc_
Code
Issues 0
Pull requests 0
Projects 1
Wiki
Insights
Settings
misc_/Open_Request_CSV.py
8bf0a3e 8 days ago
root 20180219
73 lines (53 sloc) 1.85 KB
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
This file is designed to make open request files to be able to readable.
It also able to isolate request number with *F symbols.
"""
import csv

file =input('Have you placed this program in the same location? What is the file name(+ file path)?')

with open(file,'r') as f:
    text = f.read().replace('\r\n',' ')

#Adding delimiters to headers
text = ','.join(text.split('\n'))
text = ' '.join(text.split())
text = text.replace(':',',')
text = text.replace('-',' ')
text = text.replace('Acc','\nAcc')
text = text.strip()
text = text.replace('CF',',CF,')
text = text.replace('FC',',FC,')
text = text.replace('CR',',CR')
text = text.replace('T1 B','T1, B,')
text = text.replace('T2 B','T2, B,')
text = text.replace('T3 B','T3, B,')
text = text.replace('Test',',Test')
text = text.replace('Expected',',,Expected')
text = text.replace('To',',To')
text = text.replace('VALID',',VALID')
text = text.replace('No test',',No test')
#text2csv = csv.write(csvfile, delimiter=',')

#outfile = file + '.txt'
#file = open(outfile,'w')
#file .write(text)
#file.close()

text2 = text.splitlines()


#Save full output to csv
outcsv = file + '.csv'
with open(outcsv, 'w') as g:
    mywriter = csv.writer(g,delimiter='\n', quotechar='"')
    mywriter.writerow(text2)



#Save trigger output to csv
# trigger = '*F'
# matching = [s for s in text2 if trigger in s]

# outcsvf = 'StarF_' +file  + '.csv'
# with open(outcsvf, 'w') as g:
    # mywriter = csv.writer(g,delimiter='\n', quotechar='"')
    # mywriter.writerow(matching)



# Save non-trigger output to csv
# nmatch = [s for s in text2 if trigger not in s]

# outcsvnf = 'Non_StarF_' +file  + '.csv'
# with open(outcsvnf, 'w') as g:
    # mywriter = csv.writer(g,delimiter='\n', quotechar='"')
    # mywriter.writerow(nmatch)
