
#python first program

print ('test')

import time

print('Please enter your username.')

username = input()
name = 'Matt'
if username == name	:
	print('Please Wait')
	time.sleep(1.5)
	print('')
	print('correct, please enter your password.')

if username != name:
	print('Please Wait')
	time.sleep(1.5)
	print('Incorrect, closing program')
	time.sleep(1.5)
	exit

password = input()
password1 = 'Admin'

if password == password1	:
	print('Please Wait')
	time.sleep(1.5)
	print('')
	print('Logging in')
	print('Welcome ' + username)

if password != password1	:
	print('Please Wait')
	time.sleep(1.5)
	exit




input()
