# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team204_UCusername.py
# Date: 10/26/23
# By: Meredith Bartel
# Section: Your Section
# Team: 204
#
# ELECTRONIC SIGNATURE
# Type in your name
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for
# all your python files the rest of the semester.

import math
V= float(input('Enter fluid velocity: mi/hr'))
L= float(input('Enter typical length:, M'))
u= float(input('Enter dynamic viscosity of the fluid:, kg(m*s)'))
p= float(input('Enter density of the fluid:, kg/M^3'))

L = (L/254)
V= V*.44
u= u*17.86
p= p* 27679



Re= ( p * V * L)/(u)


print ('the value of Re is {0:0.2f} \n'.format(Re))
       

