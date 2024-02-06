import math

MyData = open('Snow_Fall.txt', 'r')
Data = MyData.readlines()
MyData.close()

maxsnowfall = 0
date = ""
totdates = len(Data)
percent = 0

for line in Data:
    value = line.split()
    date_str = value[0]
    snowfall = float(value[1])
    if snowfall > maxsnowfall:
        maxsnowfall = snowfall
        date = date_str
    if snowfall > 1:
        percent += 1 / totdates * 100

print('Maximum snowfall: {0:0.2f} inches on {1}'.format(maxsnowfall, date))
print('Percentage of Days Snowfall Exceeded 1 inch: {0}%'.format(percent))
                    
        
