Y = float(input('Please enter the number of years: '))
Savings = 0
D = 1
while D < Y:
Savings = Savings + D
D = D + 1
Savings = Savings + (D+1)
for D in range(int(Y*365)):
Y = Y*365
print('Amount Saved: ${0:0.2f}'.format(Savings/100))

input('Press any key to continue.')