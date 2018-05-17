# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

This file is designed to make open request files to be able to readable.

It also able to isolate request number with *F symbols.

"""
import openpyxl

#Ask user for file name(s)
print('Have you placed this program in the same location as your files?')
print('Add all your files (+extension) you want to convert in this and separate them with a comma :?')
print('e.g. file1, file2.txt, file3, file4')
print('')
file =input('Files: ')

[print(' ') for blank in range(2)]


#Ask user for list of request number to discriminate
while True:
	check =input('Do you have a list of request numbers you wish to ignore[Y/N]')
	if check == 'Y':
		print('Have you included the file in this folder?')
		print('The file has to be formatted with one request number per line.')
		print('')
		list =input('Filename(+extension) of the list: ')
		
		with open(list,'r') as e:
			numbers = e.read().split('\n')
		numbers = ' '.join(numbers).split()
		break
		
	elif check == 'N':
		break
		
	else:
		print('This is not a valid input')
		continue



#breakdown filename for processing
file = ''.join(file.split())
file = file.split(',')
filelen = len(file)


for i in range(filelen):
    with open(file[i],'r') as f:
        text = f.read().replace('\r\n',' ')
    
    #converting the input file to a readable string
    text = text.replace(',',' ')
    text = ','.join(text.split('\n'))
    text = ' '.join(text.split())
    text = text.replace(':',',')
    text = text.replace('-',' ')
    text = text.replace('Acc',':Acc')
    text = text.strip()
    text = text.replace('CF',',CF,')
    text = text.replace('FC',',FC,')
    text = text.replace('CR',',CR')
    text = text.replace('T1 B','T1, B,')
    text = text.replace('T2 B','T2, B,')
    text = text.replace('60 B','60, B,')
    text = text.replace('T3 B','T3, B,')
    text = text.replace('Test',',Test')
    text = text.replace('Expected',',,Expected')
    text = text.replace('To',',To')
    text = text.replace('VALID',',VALID')
    text = text.replace('No test',',No test')
    text = text.replace(', ',',')
    text = text.replace(' ,',',')

    #Split string into list of strings
    text3 = [tuple(x.split(',')) for x in text.split(':')]

    #Check request number in string and delete string
    if check=='Y':

        c=[]
        for jj in range(len(numbers)):
            for ii in range(len(text3)):
                boo = numbers[jj] in text3[ii]
                if boo ==True:
                    c.append(ii)
    
        for kk in reversed(range(len(c))):
            del text3[c[kk]]        
    else:
        pass

    #Output to xls function
    wb = openpyxl.Workbook()
    ws=wb.active
    
    for row in text3:
        ws.append(row)
    
    wbsave = file[i] + ".xlsx"
    wb.save(wbsave)
    wb.close

