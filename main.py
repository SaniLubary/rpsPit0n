# Super fucking nice rock scissors paper

import time
from random import randint
import sys

# function to know the name each number refers to
def strNameRefInt(i):
	# print("name ref, val: " + str(i))
	switcher = {
		1: "Rock",
		2: "Paper",
		3: 'Scissors'
	}
	name = switcher.get(i, "Invalid number")
	return name

# if input is a digit and if its between 1-3 pass
# else, try again
def select():
	ok = False
	while ok == False:
		sPlayerChoice = input("Choose: ")								
		if sPlayerChoice.isdigit():				
			iPlayerChoice = int(sPlayerChoice)							 
			if iPlayerChoice < 1 or iPlayerChoice > 3:
				print("Choose between 1 and 3. =´]")
			else:
				ok = True
		else:
			print("Nononononon, a number, choose a number ples :]")
	return iPlayerChoice

# "wait's" for pc's response
def wait():
	x = 0
	while x < 3:
		print(".")
		time.sleep(0.25)
		x += 1

def winner(iPlayer, iPc):
	# 2 is draw, 0 is you and 1 is pc 
	# [becouse in the array, the first value is What choice you kill, and the second What choice kills you]
	result = 2

	# set winner
	if iPc == iPlayer:
		pass
	else:	
		# define possibilities
		# index 0 is the number you kill, index 1 is you die by that number
		one = [3, 2];
		two = [1, 3];
		three = [2, 1];
		
		# to define wich posibility is for the player
		# this way you select the array that corresponds to the player's selection
		switcher = {
			1: one,
			2: two,
			3: three
		}
		
		arr = switcher.get(iPlayer, "error:What paso? O.o")

		# with that array check if pc's choice kills you or gets killed by you
		for i, v in enumerate(arr):
			if v == iPc:
				result = i
				return result

	return result
	
## function start of friggin game ##
def play():
	print('IM A FUCKING SUPER NICE ROCK SCISSORS PAPER >:"]')

	print("(1) ROCK")
	print("(2) PAPER")
	print("(3) SCISSORS")

	iPcChoice = randint(1, 3)											# pc's election
	iPlayerChoice = select()											# players election

	wait()																# wait's for pc's response

	iWinner = winner(iPlayerChoice, iPcChoice)

	sPlayerChoice 	= strNameRefInt(iPlayerChoice)
	sPcChoice 		= strNameRefInt(iPcChoice)
	print( sPlayerChoice + " vs " + sPcChoice + "!!")

	# set choices to respective names of choices
	if iWinner < 2:
		if iWinner == 0:
			winMessage = "\033[0;31mYou Win!\033[0m"
		else:
			winMessage = "PC Wins!"
		print( winMessage )
	else:
		print( " Draw! ")



continuar = 1
while continuar == 1:
	play()
	response = input("Just ENTER to continue. umu \n")
	if response == "":
		pass
	else:
		continuar = 0


