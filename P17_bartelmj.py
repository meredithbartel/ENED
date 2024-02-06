#1#################################################################################

#ENED 1100 Exam 3 Problem 17 - Python Conditional
#Please fill out the info below:
#Your Name = Meredith Bartel
#Team Number = 207
#Section Number =17
#2#################################################################################
import math

speed = float(input('please enter speed of vehical(mph):'))
day = float(input('is it light outside? (enter 1 if light 2 for if dark):'))


if day == 1 and 70 > speed <= 45:
    print ('within limit')
elif day == 1 and 70 > speed >=45:
    print ('speeding')
elif day == 2 and 70 > speed <= 35:
    print('within limit')
elif day == 2 and 70 > speed>= 35:
    print ('speeding')
elif day == 2 and speed > 70:
    print ('police interception URGENT')
else:
    print ('police interception URGENT')

