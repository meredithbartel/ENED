import math

MyData = open ('Snow_Fall.txt','r')
Data = MyData.readlines()
MyData.close()

maxsnowfall = 0
date = 1
totdates = len(Data)
percent = 0

for i in Data:
    value = i.split()
    snowfall= float(value[0])
    if snowfall > i:               
        i = snowfall
        date= value[0]
    if snowfall > 1:
        percent += 1/totdates*100

print ('maximum snowfall: {0:0.2f} inches on {1}'. format(i, date))
print ('Percentage od Days Snowfall Exeeded 1 inch:{0}%'.format(percent))
                    
        
