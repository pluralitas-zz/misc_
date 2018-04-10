# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:54:33 2018

@author: aucheukyan
"""
# Import name file for query. FORMAT in text = YYYYMMDDHHmm, [NAME]
file = 'Input.txt'


with open(file,'r') as f:
    name = f.read().replace('\n',':')

name=name.replace('D/O','D O')
name=name.replace('S/O','S O')
name=name.replace('W/O','W O')
name=name.replace('A/L','A L')
    
name=[tuple(x.split(',')) for x in name.split(':')]

#Import raw file
raw =['xchrhl7040918.old','xchrhl7040818_POCT.old','xchrhl7040718_POCT.old','xchrhl7040618_POCT.old','xchrhl7040518_POCT.old','xchrhl7040418_POCT.old','xchrhl7040318_POCT.old','xchrhl7040218_POCT.old','xchrhl7040118_POCT.old','xchrhl7033118_POCT.old']
text=[]

for i in range(len(raw)):
    with open(raw[i],'r') as m:
        textraw = m.read().replace('\n','::')

    textraw=textraw.split('::')
    text = text+textraw

#Checker
c=[]
check=False
for jj in range(len(name)):
    for ii in range(len(text)):
        boo = name[jj][0] in text[ii]
        if boo ==True:
            boo2 = name[jj][1] in text[ii-3]
            if boo2==True:
                check= True
                #Change here for result output
                c.append(str(name[jj][0])+',,'+ str(name[jj][1])+',,'+ text[ii-4] +',:,'+text[ii+1]+',end')

    if check ==False:
        c.append(str(name[jj][0])+',,'+ str(name[jj][1])+',,N')
        
    elif check ==True:
        check =False
for row in c:
    row = ''.join(row)

#Remove useless info
for i in range(len(c)):
    c[i] = c[i].replace('OBX||NM|PGLU^Glucose, POCT^TTSHL||','')
    c[i] = c[i].replace('OBX||ST|PGLU^Glucose, POCT^TTSHL||','')
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0|N|||F|','')
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0|N|||I|','')
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0||||I|','')      
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0|H|||F|','')
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0|L|||F|','')
    c[i] = c[i].replace('|mmol/L|4.0 - 8.0|HH|||F|||||TTS|','')
    c[i] = c[i].replace('\r\n','')

#Remove empty results
for i in reversed(range(len(c))):
    nores = ',:,,end' in c[i]
    if nores ==True:
        del c[i]
    
#Write to output
outF = open("myOutFile.txt", "w")
for line in c:
  # write line to output file
  outF.write(line)
  outF.write("\r\n")
outF.close()