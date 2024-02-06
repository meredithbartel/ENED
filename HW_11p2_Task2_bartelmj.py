# Activity Python 1: Task 1
# File: ACT_11p2_task2_Bartelmj.py
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
#What I am going to be doing in this caod is I amcalculating and evaluating the epidemiological perameters based on the users inpuuts
#it will make decisions about public health measeurs based on calculated values

import math

sigma = float (input('Enter the coefficient sigma ='))
mu = float (input('Enter the coefficient mu ='))
gamma = float (input('Enter the coefficient gamma =:'))
delta = float (input('Enter the coefficient delta =:'))
beta_one = float (input('Enter the coefficient beta1 =:'))
beta_two = float (input('Enter the coefficient beta2 =:'))
alpha =float (input('Enter the coefficient alpha =:'))


F = (delta * (beta_one * sigma + (gamma + mu) * beta_two)) / ((sigma + mu) * (gamma + mu) * mu)
R = (1 - alpha) * F
ac = 1 - (1 / F)

if R == 1:
    if alfa < a:
        print ('Endemic State, increase public health measure')
    else:
        print ('No changege in public health measures')
elif R > 1:
    if alpha < ac:
        print ('Disease Expansion State, Increase Public Health Measures')
    else:
        print ('no change in public health measures')
elif R<1:
    if alpha > ac:
        print ('Disease controlled, Decrease public health measures')
else:
    print (' no change in public health measures')
                              
            
                 
            
        
        


 
           
