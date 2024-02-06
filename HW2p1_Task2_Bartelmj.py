####################################################################
###################Insert your header here##########################
## File: HW1p2_Task2_Bartelmj.py
# Meredith Bartel
# 1/25/2024
#ENED1120
#Setction 1.2 pythin lists and functions
#what I did in this program was I fixed the errors that were alsready made when the functions were getting defined
#and then I imported the lists and from the prevous code to then catigorize all of the numers it produced into different numbers
#and the last thing that I did was print everything out

####################################################################
def Happy(num):
    count = 0
    while num != 1 and count < 100:
        count += 1
        num0 = 0
        for digit in str(num):
            num0 += int(digit) ** 2
        num = num0
    return num == 1

def Perfect(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

def Narcissistic(num):
    Narcis = 0
    num_str = str(num)
    num_digits = len(num_str)
    for digit in num_str:
        Narcis += int(digit) ** num_digits
    return Narcis == num

######################################################################
##############Start your script here################################
N = int(input("Enter a large whole number N: "))
numbers = []
types = []
n = 1
while n <= N:
    NOtypes = ""
    if Happy(n):
        NOtypes += "h"
    if Perfect(n):
        NOtypes += "p"
    if Narcissistic(n):
        NOtypes += "n"
    numbers.append(n)
    types.append(NOtypes)
    n+= 1

for i in range(len(numbers)):
    print(f"{numbers[i]} is {types[i]}")

