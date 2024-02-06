# Activity Python 1: Task 1
# File: ACT_Python_HeaderTemplate_Team204_Bartelmj.py
# Date: 1/1/24
# By: Meredith Bartel
# Section: 10.1
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
# calculates the average grades
import math

mydata = open('Grades.txt', 'r')
data = mydata.readlines()
mydata.close()

Index = []

for line in data:
    values = line.split()
    Index.append([float(val) for val in values])

rfile = open('results.txt', 'w')
rfile.write('Index\tTotal\tLetter\n')
for r in range(len(Index)):
    RAT = Index[r][0]
    CFU = Index[r][1]
    HW = Index[r][2]
    Proj = Index[r][3]
    EXAM = Index[r][4]

    grade = 0.05 * RAT + 0.15 * CFU + 0.15 * HW + 0.20 * Proj + 0.45 * EXAM

    if 90 <= grade <= 100:
        lettergrade = 'A'
    elif 80 <= grade < 90:
        lettergrade = 'B'
    elif 70 <= grade < 80:
        lettergrade = 'C'
    elif 60 <= grade < 70:
        lettergrade = 'D'
    else:
        lettergrade = 'F'
   
    rfile.write('{0}\t{1:0.2f}\t{2}\n'.format(r + 1, grade, lettergrade))

rfile.close()



