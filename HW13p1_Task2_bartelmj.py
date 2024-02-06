
# Activity Python (Repitition): Task 2
# File: HW13p1_Task2_Bartelmj.py
# Date: 11/28/23
# By: Meredith Bartel
# Section: 13.1
# Team: 204
#
# ELECTRONIC SIGNATURE
# Meredith Bartel
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# it takes the inputed total number of blood pressure redings and it puts them into a random numers generator from numbers between 90 and 120.
#After that it will tel you how many of each reaing that it went through

import random
readings = int (input('number of BPS readings that were taken:'))
Hypo = 0
Hyper = 0
normal = 0


for k in range (readings):
    BPS = random.randint(65,140)
    if  BPS < 90:
        Hypo = Hypo + 1
    elif BPS > 120:
        Hyper = Hyper + 1
    else:
        normal = normal + 1

print ('Number of Hypotention readings: {0}\n'.format (Hypo))
print ('Number of Normal readings: {0}\n'.format (normal))
print ('Number of Hypertention readings: {0}\n'.format (Hyper))
