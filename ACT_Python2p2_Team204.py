
# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team204_Bartelmj.py
# Date: 1/2/23
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
# checks if the ph lev;e of soil is acidic nutral basic or invalid
# get the value for user
Ph = int (input('please enter the PH of the soil:'))
if 0 <= Ph and Ph < 7:
   print (' acidic')
elif Ph == 7:
    print (' neutral')
elif 7 < Ph and Ph <=14:
    print (' Basic')
else:
    print (' invalid')
    
