#buysell.py

import time
import string

eighthAmount = 35
quarterAmount = 75
halfAmount = 120
gramAmount = 10




#buyer chooses amount to buy here 
def amountSelection(userAmount):
	if userAmount == 'g':
		choice = 0
		print 'Thank you for purchasing a gram'
	elif userAmount == 'e':
		choice = 1
		print 'Thank you for purchasing an eighth'
	elif userAmount == 'q':
		choice = 2
		print 'Thank you for purchasing a quarter'
	elif userAmount == 'h':
		choice = 3
		print 'Thank you for purchasing a gram'
	else:
		choice = -1
		print 'test'

	return choice






def Checkout(userChoice):
	if userChoice ==0:
		price = gramAmount
	elif userChoice ==1:
		price =	eighthAmount
	elif userChoice ==2:
		price = quarterAmount
	elif userChoice ==3:
		price = halfAmount
	else:
		print 'invalid choice'
	return price






def payment(userPayment,userWallet):
	owesMoney = True
	amountOwed = userWallet
	amountTendered = userPayment
	change = 0

	while owesMoney:
		if amountTendered == amountOwed:
			print 'Good'
			owesMoney = False

		elif amountTendered > amountOwed:
			change = amountTendered - amountOwed
			print 'Change: ' + str(change)
			owesMoney = False

		elif amountTendered < amountOwed:
			amountOwed = amountOwed - amountTendered
			print 'Not enough. Please input ' + str(amountOwed) + ' or MOAR! '
			amountTendered = input()







userChoice = -1
userWallet = 0  

print('Thank you for contacting The Plug!\nWe here in Colorado appreciate your support')
time.sleep(.3)
print ('How much are you purchasing today?\nOur selection includes dank prices from a gram to a half ounce!')
time.sleep(.3)
print('Please input the size\ng for a gram\ne for eighth\nq for quarter\nh for half')

userAmount = string.lower(raw_input())

userChoice = amountSelection(userAmount)

userWallet = Checkout(userChoice)

print 'Your total is: '
print userWallet
print 'Please input your payment'

userPayment = input()

payment(userPayment,userWallet)















