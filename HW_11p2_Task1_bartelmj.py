# Activity Python 1: Task 1
# File: ACT_11p2_task 1_Bartelmj.py
# Date: 11/16/23
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
#description
#what i am doing in this is the users inputs their ages, wheight, current heart rate
#and machine type  and the program calculates and outputs the exercise intensity level and
#calories burned per hour based on the provided equations and
#user inputs, displaying the results with two decimal points in a single print statement
#
import math
age = float (input('please enter users age:'))
weight = float (input('please enter users weight in pounds:'))
CHR = float (input('please enter users current heart rate in beats/minutes:'))
machine_type = input("please enter the type of machine:(manual/automatic)")

if machine_type == "automatic":
    calories_burned_per_hour = 60 * ((age*0.2017+weight * 0.09036 +CHR * 0.4472 -20.4022)/4.184)
    MHR = 206 - 0.65 * age
    print ('Calories burnt per hour is: {0:.2f}'.format (calories_burned_per_hour))
elif machine_type == "manual":
    calories_burned_per_hour = 60 * ((age*0.074-weight*0.05741+CHR*0.4472-20.4022)/4.184)
    MHR = 205.8 - 0.685 * age
    print ('Calories burnt per hour is: {0:.2f}'.format (calories_burned_per_hour))


sixty_percent_mhr = 0.6 * MHR
seventy_percent_mhr = 0.7 * MHR
eighty_percent_mhr = 0.8 * MHR
ninty_percent_mhr = 0.9 * MHR

if CHR < sixty_percent_mhr < MHR:
    print ('Below level')
if sixty_percent_mhr <= CHR <= seventy_percent_mhr:
    print ('weight loss')
if  seventy_percent_mhr <= CHR <= eighty_percent_mhr:
    print ('cario')
if eighty_percent_mhr <= CHR <= ninty_percent_mhr:
    print ('anaerobic (hardcore)')
if CHR >= ninty_percent_mhr:
    print ('above level')
    

             
