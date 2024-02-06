

#1#################################################################################
2
#ENED 1100 Exam 3 Problem 18 - Python Repetition
#Please fill out the info below:
#Your Name =
#Team Number =
#Section Number =
#2##########################################################################
import math


Y = float (input('input values for for veriable,y:'))
N = float (input('input values for for veriable,N:'))

X=3

while N < 200:
    N = N
#while loops automaticy incriment by 1 so itll repeat unill it hit 200
    while Y < N:
        if X < 7:
            X = X + 3
        else:
            X = X - 2 
    Y = X**2 + 3**Y
    print ('x = {0:0.2f}\n'.format(X))
    print ('y = {0:0.2f}\n'.format(Y))
 

    
       


        
