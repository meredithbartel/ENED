# Activity Python (Repitition): Task 3
# File: HW13p1_Task3_Bartelmj.py
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
# This Python program identifies and counts prime numbers and perfect numbers within the range
#from 2 to the user-input whole number K, printing the results.
import math

K = int(input("Enter a whole number: "))

C1 = 0
C2 = 0

for n in range(2, K):
    S = 0
    m = math.ceil(n / 2) + 1
    
    for p in range(2, m):
        R = n % p
        if R == 0:
            S = S + p  # accumulate divisors

    if S == 0:
        print(f"The number n = {n} is prime")
        C1 += 1
    elif S == n - 1:
        print(f"The number n = {n} is perfect")
        C2 = C2 + 1

print(f"The total number of prime numbers found is C1 = {C1}")
print(f"The total number of perfect numbers found is C2 = {C2}")


