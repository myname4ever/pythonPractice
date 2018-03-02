#This is a backup file
#buysell.py

import time
import string


eighthAmount = 35
quarterAmount = 75
halfAmount = 120
gramAmount = 10
userChoice = -1

print('Thank you for contacting The Plug!\nWe here in Colorado appreciate your support')
time.sleep(.3)
print ('How much are you purchasing today?\nOur selection includes dank prices from a gram to a half ounce!')
time.sleep(.3)
print('Please input the size\ng for a gram\ne for eighth\nq for quarter\nh for half')

userAmount = string.lower(raw_input())
userWallet = 0  


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


userChoice = amountSelection(userAmount)


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


userWallet = Checkout(userChoice)

print 'Your total is: '
print userWallet
print 'Please input your payment'

userPayment = input()

def payment(userPayment,userWallet):
	if userPayment == userWallet:
		print 'Thank you for your business!'
	
	elif userPayment < userWallet:
		while userPayment < userWallet:
			print 'Please input the following amount: ' + str(userWallet - 	userPayment)
			userChange = input()
			userPayment + userChange
	
	elif userPayment > userWallet:
		print 'Here is your change. Thank you for your busniness!'
		print str(userPayment - userWallet)

payment(userPayment,userWallet)
