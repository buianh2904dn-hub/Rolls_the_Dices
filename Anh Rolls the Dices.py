import time
time.sleep(1)
print("Hello! Welcome to play rolling the dice :)")
time.sleep(1)
print("The rule be showed as well as the instruction while you playing.")
time.sleep(1)
print("Now let's get started!!!")

time.sleep(1)
import random

def ask_ques1():
	ask1 = input("How many dices you want to roll? (Choose between 1 and 2 dice) \n")
	num = int(ask1)
	return num
	
def ask_ques2():
	ask2 =input("How many sides of the dice that you want to roll? (Can choose between 2 and 256)\n")
	side = int(ask2)
	return side

def ans():
	ans = print("The numbers are: " + str(dice))
	return ans

again = 'yes'
while again == 'yes' or again == 'y':
	dice = random.randint(5,500)
	num = ask_ques1()
	
	if num == 1:
		side = ask_ques2()
		if side <= 1:
			print("Impossible. Please try a higher side")
			guess = int(input("How many sides of the dice that you want to roll? (Can choose between 2 and 256)\n"))
			if guess <= 1:
				print("Sorry, the side is too low.")
			elif guess > 256:
				print("Sorry, the side is too high.")
			else:
				ans()
		elif 1 < side <= 256 and side // 2 == 0:
			ans()
		else:
			if side > 256:
				print("Sorry, the side is too high...")
				side = ask_ques2()
				if side <= 1:
					print("Unfortunately, the side is too low...")
				elif side > 256:
					print("Unfortunately, the side is high again.")
				else:
					ans()
			elif side <= 1:
				print("Sorry, the side is too low...")
				side = ask_ques2()
				if side <= 1:
					print("Unfortunately, the side is low again.")
				elif side > 256:
					print("Unfortunately, the side is high.")
				else:
					ans()
			else:
				ans()
	else:
		if num == 2:
			side = ask_ques2()
			if side <= 1:
				print("Impossible. Please try a higher side")
				side = int(input("How many sides of the dice that you want to roll? (Can choose between 2 and 256)\n"))
				if 1 < side <= 256 and side // 2 == 0:
					ans()
				else:
					if side > 256:
						print("Sorry, the side is too high.")
						side = ask_ques2()
						if side <= 1:
							print("Unfortunately, the side is too low...")
						elif side > 256:
							print("Unfortunately, the side is high again.")
						else:
							ans()
					elif side <= 1:
						print("Sorry, the side is too low...")
						side = ask_ques2()
						if side <= 1:
							print("Unfortunately, the side is low again.")
						elif side > 256:
							print("Unfortunately, the side is high.")
						else:
							ans()
					else:
						ans()
			elif 1 < side <= 256 and side // 2 == 0:
				ans()
			else:
				if side > 256:
					print("Sorry, the side is too high.")
					side = ask_ques2()
					if side <= 1:
						print("Unfortunately, the side is too low...")
					elif side > 256:
						print("Unfortunately, the side is high again.")
					else:
						ans()
				else:
					ans()
		else:
			print("Only choose between 1 and 2 dice!")
			num = int(input("How many dice you want to roll?\n"))
			if num == 1:
				side = ask_ques2()
				if side > 256:
					print("The side is too high :(")
					print("Let's try again")
					guess = ask_ques2()
					if side > 256:
						print("Sorry, the side is high again.")
					elif side < 2:
						print("Sorry, the side is too low.")
					else:
						ans()
				elif side <= 1:
					print("The side is too low :(")
					print("Let's try again")
					guess = ask_ques2()
					if side > 256:
						print("Sorry, the side is too high.")
					elif side < 2:
						print("Sorry, the side is low again.")
					else:
						ans()
				else:
					ans()
			elif num == 2:
				side = ask_ques2()
				if side > 256:
					print("The side is too high :(")
					print("Let's try again")
					guess = ask_ques2()
					if side > 256:
						print("Sorry, the side is high again.")
					elif side < 2:
						print("Sorry, the side is too low.")
					else:
						ans()
				elif side <= 1:
					print("The side is too low :(")
					print("Let's try again")
					guess = ask_ques2()
					if side > 256:
						print("Sorry, the side is too high.")
					elif side < 2:
						print("Sorry, the side is low again.")
					else:
						ans()
				else:
					ans()
			else:
				print("Impossible to roll the dice !!!")
		
	again = input("Do you want to play again? (Y/N)\n").lower()
time.sleep(1)
print("Thanks for playing.")
time.sleep(1)
print("Program ended.")

