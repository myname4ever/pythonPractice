import time

print '4..'
time.sleep(2)
print '2..'
time.sleep(2)
print '0'
time.sleep(2)
print('Fire in the bowl')
time.sleep(2)
print ('Are you there?')

userResponse = raw_input()
correctAnswer = 'yes'

if userResponse == correctAnswer:
 	print('Bet!')
else:
	print('that sucks')

time.sleep(1)
quit()
