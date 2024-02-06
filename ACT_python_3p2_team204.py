# Activity Python 1: Task 2
# File: ACT_Python_3p2_Team204_Bartelmj.py
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
#
import math
import random
T = int (input('please enter number of time the coin was fliped:'))

F = 1
tails = 0
heads = 1
for X in range(T):
    F = random.randint(0,1)
    if F == 1:
        heads = heads + 1
    else:
        tails = tails + 1
Percent_tails = tails / T
percent_heads = heads / T

print (' the percentage of flips landed on tails is:'.format (percent_tail))
print (' the percentage of flips landed on head is:'.format (percent_heads))



