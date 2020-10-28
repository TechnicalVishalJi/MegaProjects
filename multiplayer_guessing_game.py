import random

print("Guess Game\n")

p1 = input ("Player 1 enter your name.\n")
p2 = input ("Player 2 enter your name.\n")

list = []

def main(player , player2):
	tchances = int(input("Enter number of chances\n"))
	global list
	
	chances = tchances
	a = int(input(f"{player} - Enter first number\n"))
	b = int(input(f"{player} - Enter second number\n"))
	randnum = random.randint(a,b)
	'''Game will start now'''
	while chances>0:
		try:
			guess = int(input(f"{player2} - Enter your guess\n"))
		except Exception as e:
			print("Please enter only numbers\n")
				
		else:
			if guess==randnum:
				print("You guessed the correct number!\n")
				chances -= 1
				break
			elif guess>randnum:
				print("You guessed greater number\nTry again\n")
				chances -= 1
				continue
			elif guess<randnum:
				print("You guessed smaller number\nTry again\n")
				chances -= 1
				continue
	ct = tchances - chances
	list.append(ct)
	print(player2, " took ", ct , " chances\n")
	
main(p1,p2)
main(p2, p1)
def results():
	fs = list[0]
	ls = list[1]
	if fs == ls:
		print("No one won in this game\n")
	elif fs < ls:
		print(f"{p2} won")
	elif fs > ls:
		print(f"{p1} won")
	else:
		print("Error!")
results()
						
choice = input("Do you want to play again? 'yes' or 'no'\n")
if choice=="yes":
	list.pop()
	list.pop()
	main(p1,p2)
	main(p2, p1)
	results()
else:
	exit()